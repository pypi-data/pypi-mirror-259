"""
Concrete :class:`~.base.TrackerJobsBase` subclass for PTP
"""

import functools
import re
from datetime import datetime

from ... import errors, jobs, uis, utils
from ...utils.release import ReleaseType
from ..base import TrackerJobsBase
from . import metadata

import logging  # isort:skip
_log = logging.getLogger(__name__)


class PtpTrackerJobs(TrackerJobsBase):

    @functools.cached_property
    def jobs_before_upload(self):
        # NOTE: Keep in mind that the order of jobs is important for
        #       isolated_jobs: The final job is the overall result, so if
        #       upload_screenshots_job is listed after description_job,
        #       --only-description is going to print the list of uploaded
        #       screenshot URLs.
        return (
            # Common interactive jobs
            self.type_job,
            self.imdb_job,
            self.source_job,
            # self.video_codec_job,
            # self.container_job,
            # self.resolution_job,
            self.scene_check_job,

            # Interactive jobs that only run if movie does not exists on PTP yet
            self.title_job,
            self.year_job,
            self.edition_job,
            self.plot_job,
            self.tags_job,
            self.poster_job,

            # Background jobs
            self.create_torrent_job,
            self.mediainfo_job,
            self.screenshots_job,
            self.upload_screenshots_job,
            self.ptp_group_id_job,
            self.audio_languages_job,
            self.subtitle_languages_job,
            self.trumpable_job,
            self.description_job,
        )

    @property
    def isolated_jobs(self):
        """
        Sequence of job attribute names (e.g. "title_job") that were singled
        out by the user, e.g. with --only-title
        """
        if self.options.get('only_description', False):
            return self.get_job_and_dependencies(
                self.description_job,
                # `screenshots_job` is needed by `upload_screenshots_job`, but
                # `upload_screenshots_job` is a `QueueJobBase`, which doesn't
                # know anything about the job it gets input from and therefore
                # can't tells us that it needs `screenshots_job`.
                self.screenshots_job,
            )
        else:
            # Activate all jobs in jobs_before/after_upload
            return ()

    @functools.cached_property
    def type_job(self):
        return jobs.dialog.ChoiceJob(
            name=self.get_job_name('type'),
            label='Type',
            precondition=self.make_precondition('type_job'),
            autodetect=self.autodetect_type,
            options=(
                ('Feature Film', 'Feature Film'),
                ('Short Film', 'Short Film'),
                ('Miniseries', 'Miniseries'),
                ('Stand-up Comedy', 'Stand-up Comedy'),
                ('Live Performance', 'Live Performance'),
                ('Movie Collection', 'Movie Collection'),
            ),
            callbacks={
                'finished': self.update_imdb_query,
            },
            **self.common_job_args(),
        )

    def autodetect_type(self, _):
        if self.release_name.type == ReleaseType.season:
            return 'Miniseries'

        # Short film if runtime 45 min or less (Rule 1.1.1)
        # NOTE: This doesn't work for VIDEO_TS releases. We could sum the
        #       duration of all .VOB files, but they notoriously lie about their
        #       duration. For now, the user can always correct the autodetected
        #       type.
        main_video = tuple(utils.video.filter_main_videos(
            tuple(utils.video.find_videos(self.content_path))
        ))[0]
        if utils.video.duration(main_video) <= 45 * 60:
            return 'Short Film'

    @functools.cached_property
    def imdb_job(self):
        imdb_job = super().imdb_job
        # Disabled until #7 is fixed.
        imdb_job.no_id_ok = False
        return imdb_job

    def update_imdb_query(self, type_job_):
        """
        Set :attr:`~.webdbs.common.Query.type` on
        :attr:`~.TrackerJobsBase.imdb_job` to :attr:`~.ReleaseType.movie` or
        :attr:`~.ReleaseType.series` depending on the output of :attr:`type_job`
        """
        assert self.type_job.is_finished
        if self.type_job.output:
            new_type = self.type_job.output[0]
            if new_type == 'Feature Film':
                _log.debug('Updating IMDb query type: %r', utils.release.ReleaseType.movie)
                self.imdb_job.query.type = utils.release.ReleaseType.movie
            elif new_type == 'Miniseries':
                _log.debug('Updating IMDb query type: %r', utils.release.ReleaseType.series)
                self.imdb_job.query.type = utils.release.ReleaseType.series

    @functools.cached_property
    def audio_languages_job(self):
        return jobs.custom.CustomJob(
            name=self.get_job_name('audio-languages'),
            label='Audio Languages',
            precondition=self.make_precondition('audio_languages_job'),
            worker=self.autodetect_audio_languages,
            no_output_is_ok=True,
            catch=(
                errors.ContentError,
            ),
            **self.common_job_args(ignore_cache=True),
        )

    async def autodetect_audio_languages(self, job):
        audio_languages = utils.video.languages(
            self.content_path,
            default='?',
            exclude_commentary=True,
        ).get('Audio', ())
        _log.debug('Audio languages: %r', audio_languages)
        for language in audio_languages:
            self.audio_languages_job.send(language)

    @functools.cached_property
    def subtitle_languages_job(self):
        return jobs.custom.CustomJob(
            name=self.get_job_name('subtitle-languages'),
            label='Subtitle Languages',
            precondition=self.make_precondition('subtitle_languages_job'),
            worker=self.autodetect_subtitle_languages,
            no_output_is_ok=True,
            **self.common_job_args(ignore_cache=True),
        )

    async def autodetect_subtitle_languages(self, job):
        # Unlike video.languages(), the subtitles property from the parent class
        # includes external subtitles, e.g. from .srt or .idx/.sub files.
        subtitle_languages = [
            subtitle.language or '?'
            for subtitle in self.subtitles
        ]
        _log.debug('Subtitle languages: %r', subtitle_languages)
        for language in subtitle_languages:
            self.subtitle_languages_job.send(language)

        # If there are any subtitle tracks without a language tag, tell the user
        # to manually check the subtitle boxes on the website.
        if '?' in subtitle_languages:
            self.subtitle_languages_job.warn(
                "Some subtitle tracks don't have a language tag.\n"
                'Please add any missing subtitle languages manually\n'
                'on the website after uploading.'
            )

    @functools.cached_property
    def trumpable_job(self):
        return jobs.custom.CustomJob(
            name=self.get_job_name('trumpable'),
            label='Trumpable',
            precondition=self.make_precondition('trumpable_job'),
            prejobs=(
                self.audio_languages_job,
                self.subtitle_languages_job,
            ),
            worker=self.autodetect_trumpable,
            no_output_is_ok=True,
            **self.common_job_args(ignore_cache=True),
        )

    async def autodetect_trumpable(self, job):
        reasons = []

        if self.options.get('hardcoded_subtitles', None) in (True, False):
            # User specified "Hardcoded subtitles"
            if self.options['hardcoded_subtitles']:
                reasons.append(metadata.PtpTrumpableReason.HARDCODED_SUBTITLES)
        # Autodetection of hardcoded subtitles would go here

        if self.options.get('no_english_subtitles', None) in (True, False):
            # User specified "No English subtitles"
            if self.options['no_english_subtitles']:
                reasons.append(metadata.PtpTrumpableReason.NO_ENGLISH_SUBTITLES)
        else:
            # Autodetect "No English subtitles"
            assert self.audio_languages_job.is_finished
            assert self.subtitle_languages_job.is_finished
            audio_languages = self.audio_languages_job.output
            subtitle_languages = self.subtitle_languages_job.output
            if (
                    # Not a silent film?
                    audio_languages
                    # No properly tagged English audio track?
                    and 'en' not in audio_languages
            ):
                # English subtitles are required.
                if 'en' not in subtitle_languages:
                    # No English subtitles found. If there are any audio or
                    # subtitle tracks that could be English, ask the user.
                    prompt = self.get_trumpable_no_english_subtitles_prompt(audio_languages, subtitle_languages)
                    if prompt:
                        self.trumpable_job.add_prompt(prompt)
                    else:
                        # Every audio and subtitle track has a language tag and
                        # none of them are English.
                        reasons.append(metadata.PtpTrumpableReason.NO_ENGLISH_SUBTITLES)

        _log.debug('Trumpable reasons from autodetection: %r', reasons)
        return reasons

    def get_trumpable_no_english_subtitles_prompt(self, audio_languages, subtitle_languages):
        audio_languages = self.audio_languages_job.output
        subtitle_languages = self.subtitle_languages_job.output
        question = ''

        if '?' in audio_languages and '?' in subtitle_languages:
            question = (
                'Does this release have an English audio track or\n'
                'English subtitles for the main audio track?\n'
                '(Commentary and the like do not count.)'
            )

        elif '?' in audio_languages:
            question = (
                'Does this release have an English audio track?\n'
                '(Commentary and the like do not count.)'
            )

        elif '?' in subtitle_languages:
            question = 'Does this release have English subtitles for the main audio track?'

        if question:
            return uis.prompts.RadioListPrompt(
                question=question,
                options=(
                    ('Yes', None),
                    ('No', metadata.PtpTrumpableReason.NO_ENGLISH_SUBTITLES),
                ),
                callbacks=(
                    self.trumpable_no_english_subtitles_prompt_callback,
                ),
            )

    def trumpable_no_english_subtitles_prompt_callback(self, answer):
        _log.debug('Trumpable rasons from user: %r', answer)
        text, reason = answer
        if reason:
            self.trumpable_job.send(reason)

    @functools.cached_property
    def description_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('description'),
            label='Description',
            precondition=self.make_precondition('description_job'),
            prejobs=self.get_job_and_dependencies(
                self.mediainfo_job,
                self.upload_screenshots_job,
            ),
            text=self.generate_description,
            read_only=True,
            hidden=True,
            finish_on_success=True,
            **self.common_job_args(ignore_cache=True),
        )

    async def generate_description(self):
        original_release_name = (
            '[size=4]'
            + '[b]'
            + utils.fs.basename(
                utils.fs.strip_extension(self.content_path)
            )
            + '[/b]'
            + '[/size]'
        )

        # Join mediainfos + screenshots for each movie/episode into
        # sections. Each section may contain multiple mediainfos (.IFO/.VOB).
        tags = []
        subtags = []
        for video_path, info in self.mediainfos_and_screenshots.items():
            if info['mediainfo']:
                subtags.append(f'[mediainfo]{info["mediainfo"]}[/mediainfo]')
            if info['screenshot_urls']:
                subtags.append('\n'.join(
                    f'[img={url}]'
                    for url in info['screenshot_urls']
                ))
                tags.append(''.join(subtags))
                subtags.clear()

        description = (
            original_release_name
            + '\n\n'
            + '\n[hr]\n'.join(tags)
        )
        return description

    mediainfo_from_all_videos = True
    screenshots_from_all_videos = True

    @functools.cached_property
    def screenshots_count(self):
        """
        How many screenshots to make

        Use :attr:`options`\\ ``["screenshots"]`` it it exists. This value
        should be explicitly set by the user, e.g. via a CLI argument or GUI
        element.

        Use :attr:`options`\\ ``["screenshots_from_movie"]`` for uploads that
        contain a single video file.

        Use :attr:`options`\\ ``["screenshots_from_episode"]`` for uploads that
        contain multiple video files.
        """
        # CLI option, GUI widget, etc
        if self.options.get('screenshots'):
            return self.options['screenshots']

        # Get that same video files that were passed to ScreenshotsJob in
        # JobBase.screenshots_job.
        video_files = utils.torrent.filter_files(
            self.content_path,
            exclude=self.exclude_files,
        )
        # Exclude samples, extras, DVD menus, etc
        video_files = utils.video.filter_main_videos(video_files)
        if len(video_files) == 1:
            return self.options['screenshots_from_movie']
        else:
            return self.options['screenshots_from_episode']

    @functools.cached_property
    def ptp_group_id_job(self):
        return jobs.custom.CustomJob(
            name=self.get_job_name('ptp-group-id'),
            label='PTP Group ID',
            precondition=self.make_precondition('ptp_group_id_job'),
            prejobs=self.get_job_and_dependencies(
                self.imdb_job,
            ),
            worker=self.get_ptp_group_id,
            catch=(
                errors.RequestError,
            ),
            **self.common_job_args(),
        )

    async def get_ptp_group_id(self, _):
        # Get group ID from PTP by IMDb ID.
        assert self.imdb_job.is_finished, self.imdb_job
        group_id = await self.tracker.get_ptp_group_id_by_imdb_id(self.imdb_id)
        if group_id:
            _log.debug('PTP group ID via IMDb ID: %r -> %r', self.imdb_id, group_id)
            return group_id
        else:
            # If there is no existing PTP group, ask the user. Usually this
            # happens if PTP doesn't know this movie yet. The user can just
            # press enter to create a new PTP group.
            #
            # But it's also possible that PTP has a group for this movie while
            # it has no IMDb ID.
            self.ptp_group_id_job.add_prompt(uis.prompts.TextPrompt(
                callbacks=(
                    self.ptp_group_id_prompt_callback,
                ),
            ))
            self.ptp_group_id_job.info = 'Leave this empty to create a new PTP group.'

    def ptp_group_id_prompt_callback(self, ptp_group_id):
        _log.debug('PTP group ID from user: %r', ptp_group_id)
        self.ptp_group_id_job.send(ptp_group_id.strip())

    @property
    def ptp_group_id(self):
        """
        PTP group ID if :attr:`ptp_group_id_job` is finished and group ID
        was found, `None` otherwise
        """
        if self.ptp_group_id_job.is_finished:
            if self.ptp_group_id_job.output:
                return self.ptp_group_id_job.output[0]

    def ptp_group_does_not_exist(self):
        """
        Whether no releases of :attr:`imdb_id` already exist

        :attr:`ptp_group_id_job` must be finished when this is called.

        This is used as a :attr:`~.JobBase.precondition` for jobs that are only
        needed if the server doesn't have any releases for this :attr:`imdb_id`
        yet.
        """
        assert self.ptp_group_id_job.is_finished, self.ptp_group_id_job
        if self.ptp_group_id:
            return False
        else:
            return True

    @functools.cached_property
    def title_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('title'),
            label='Title',
            precondition=self.make_precondition(
                'title_job',
                # Don't run this job if PTP already knows this movie.
                precondition=self.ptp_group_does_not_exist,
            ),
            prejobs=self.get_job_and_dependencies(
                # We need to wait for the PTP group ID to become available
                # before we can check if it exists.
                self.ptp_group_id_job,
            ),
            text=self.fetch_title,
            normalizer=self.normalize_title,
            validator=self.validate_title,
            **self.common_job_args(),
        )

    async def fetch_title(self):
        assert self.imdb_job.is_finished, self.imdb_job
        return await self.tracker.get_ptp_metadata(self.imdb_id, key='title')

    def normalize_title(self, text):
        return text.strip()

    def validate_title(self, text):
        if not text:
            raise ValueError('Title must not be empty.')

    @functools.cached_property
    def year_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('year'),
            label='Year',
            precondition=self.make_precondition(
                'year_job',
                # Don't run this job if PTP already knows this movie.
                precondition=self.ptp_group_does_not_exist,
            ),
            prejobs=self.get_job_and_dependencies(
                # We need to wait for the PTP group ID to become available
                # before we can check if it exists.
                self.ptp_group_id_job,
            ),
            text=self.fetch_year,
            normalizer=self.normalize_year,
            validator=self.validate_year,
            **self.common_job_args(),
        )

    async def fetch_year(self):
        assert self.imdb_job.is_finished, self.imdb_job
        return await self.tracker.get_ptp_metadata(self.imdb_id, key='year')

    def normalize_year(self, text):
        return text.strip()

    def validate_year(self, text):
        if not text:
            raise ValueError('Year must not be empty.')
        try:
            year = int(text)
        except ValueError:
            raise ValueError('Year is not a number.')
        else:
            if not 1800 < year < datetime.now().year + 10:
                raise ValueError('Year is not reasonable.')

    @functools.cached_property
    def edition_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('edition'),
            label='Edition',
            precondition=self.make_precondition('edition_job'),
            text=self.autodetect_edition,
            finish_on_success=True,
            **self.common_job_args(ignore_cache=True),
        )

    async def autodetect_edition(self):
        # List of keys in metadata.ptp_editions. The corresponding values are
        # returned in the same order as they are specified in
        # metadata.ptp_editions.
        edition_keys = []

        for key, is_edition in self.autodetect_edition_map.items():
            if is_edition(self):
                edition_keys.append(key)

        return ' / '.join(
            metadata.ptp_editions[key]
            for key in edition_keys
        )

    autodetect_edition_map = {
        'collection.criterion': lambda self: 'Criterion' in self.release_name.edition,
        # 'collection.masters': lambda self: False,
        # 'collection.warner': lambda self: False,

        'edition.dc': lambda self: "Director's Cut" in self.release_name.edition,
        'edition.extended': lambda self: 'Extended Cut' in self.release_name.edition,
        # 'edition.rifftrax': lambda self: False,
        'edition.theatrical': lambda self: 'Theatrical Cut' in self.release_name.edition,
        'edition.uncut': lambda self: 'Uncut' in self.release_name.edition,
        'edition.unrated': lambda self: 'Unrated' in self.release_name.edition,

        'feature.remux': lambda self: 'Remux' in self.release_name.source,
        'feature.2in1': lambda self: '2in1' in self.release_name.edition,
        # 'feature.2disc': lambda self: False,
        # 'feature.3d_anaglyph': lambda self: False,
        # 'feature.3d_full_sbs': lambda self: False,
        # 'feature.3d_half_ou': lambda self: False,
        # 'feature.3D_half_sbs': lambda self: False,
        'feature.4krestoration': lambda self: '4k Restored' in self.release_name.edition,
        'feature.4kremaster': lambda self: '4k Remastered' in self.release_name.edition,
        'feature.10bit': lambda self: (
            utils.video.bit_depth(self.content_path, default=None) == 10
            and 'HDR' not in self.release_name.hdr_format
            and 'DV' not in self.release_name.hdr_format
        ),
        # 'feature.extras': lambda self: False,
        # 'feature.2d3d_edition': lambda self: False,
        'feature.dtsx': lambda self: 'DTS:X' in self.release_name.audio_format,
        'feature.dolby_atmos': lambda self: 'Atmos' in self.release_name.audio_format,
        'feature.dolby_vision': lambda self: 'DV' in self.release_name.hdr_format,
        'feature.hdr10': lambda self: re.search(r'HDR10(?!\+)', self.release_name.hdr_format),
        'feature.hdr10+': lambda self: 'HDR10+' in self.release_name.hdr_format,
        'feature.dual_audio': lambda self: self.release_name.has_dual_audio,
        # 'feature.english_dub': lambda self: False,
        'feature.commentary': lambda self: self.release_name.has_commentary,
    }

    @functools.cached_property
    def tags_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('tags'),
            label='Tags',
            precondition=self.make_precondition(
                'tags_job',
                # Don't run this job if PTP already knows this movie.
                precondition=self.ptp_group_does_not_exist,
            ),
            prejobs=self.get_job_and_dependencies(
                # We need to wait for the PTP group ID to become available
                # before we can check if it exists.
                self.ptp_group_id_job,
            ),
            text=self.fetch_tags,
            normalizer=self.normalize_tags,
            validator=self.validate_tags,
            **self.common_job_args(),
        )

    async def fetch_tags(self):
        assert self.imdb_job.is_finished, self.imdb_job
        return await self.tracker.get_ptp_metadata(self.imdb_id, key='tags')

    def normalize_tags(self, text):
        tags = [tag.strip() for tag in text.split(',')]
        deduped = sorted(dict.fromkeys(tags))
        return ', '.join(tag for tag in deduped if tag)

    def validate_tags(self, text):
        for tag in text.split(','):
            tag = tag.strip()
            if tag and tag not in metadata.ptp_tags:
                raise ValueError(f'Tag is not valid: {tag}')

    @functools.cached_property
    def poster_job(self):
        job = super().poster_job
        # Hide poster_job until imdb_job and ptp_group_id_job are done.
        job.prejobs += (
            self.imdb_job,
            self.ptp_group_id_job,
        )
        return job

    async def get_poster_from_tracker(self):
        """Get poster URL from PTP API"""
        await self.imdb_job.wait()
        _log.debug('Getting poster from PTP API: %r', self.imdb_id)
        poster = await self.tracker.get_ptp_metadata(self.imdb_id, key='art')
        if poster:
            # Return original poster URL without resizing or re-uploading.
            return {
                'poster': poster,
                'width': None,
                'height': None,
                'imghosts': (),
                'write_to': None,
            }

    @functools.cached_property
    def plot_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('plot'),
            label='Plot',
            precondition=self.make_precondition(
                'plot_job',
                # Don't run this job if PTP already knows this movie.
                precondition=self.ptp_group_does_not_exist,
            ),
            prejobs=self.get_job_and_dependencies(
                # We need to wait for the PTP group ID to become available
                # before we can check if it exists.
                self.ptp_group_id_job,
            ),
            text=self.fetch_plot,
            normalizer=self.normalize_plot,
            validator=self.validate_plot,
            finish_on_success=True,
            **self.common_job_args(),
        )

    async def fetch_plot(self):
        assert self.imdb_job.is_finished, self.imdb_job
        return await self.tracker.get_ptp_metadata(self.imdb_id, key='plot')

    def normalize_plot(self, text):
        return text.strip()

    def validate_plot(self, text):
        if not text:
            raise ValueError('Plot must not be empty.')

    @functools.cached_property
    def source_job(self):
        return jobs.dialog.TextFieldJob(
            name=self.get_job_name('source'),
            label='Source',
            precondition=self.make_precondition('source_job'),
            text=self.autodetect_source,
            normalizer=self.normalize_source,
            validator=self.validate_source,
            finish_on_success=True,
            **self.common_job_args(),
        )

    _known_sources = {
        'Blu-ray': re.compile(r'(?i:blu-?ray)'),  # (UHD) BluRay (Remux)
        'DVD': re.compile(r'^(?i:dvd)'),  # DVD(Rip|5|9|...)
        'WEB': re.compile(r'^(?i:web)'),  # WEB(-DL|Rip)
        'HD-DVD': re.compile(r'^(?i:hd-?dvd)$'),
        'HDTV': re.compile(r'^(?i:hd-?tv)$'),
        'TV': re.compile(r'^(?i:tv)'),  # TV(Rip|...)
        'VHS': re.compile(r'^(?i:vhs)'),  # VHS(Rip|...)
    }

    def autodetect_source(self):
        # Find autodetected source in valid PTP sources
        source = self.release_name.source
        for known_source, regex in self._known_sources.items():
            if regex.search(source):
                # Finish the job without prompting the user
                return known_source

        # Let the user fix the autodetected source
        self.source_job.text = source

    def normalize_source(self, text):
        text = text.strip()
        for source in self._known_sources:
            if source.casefold() == text.casefold():
                return source
        return text

    def validate_source(self, text):
        if not text or text == 'UNKNOWN_SOURCE':
            raise ValueError('You must provide a source.')
        elif text not in self._known_sources:
            raise ValueError(f'Source is not valid: {text}')

    # # POST parameter "codec" seems to be optional.

    # @functools.cached_property
    # def video_codec_job(self):
    #     return jobs.dialog.TextFieldJob(
    #         name=self.get_job_name('video_codec'),
    #         label='Video Codec',
    #         precondition=self.make_precondition('video_codec_job'),
    #         text=self.autodetect_video_codec,
    #         finish_on_success=True,
    #         normalizer=self.normalize_video_codec,
    #         validator=self.validate_video_codec,
    #         **self.common_job_args(),
    #     )

    # def autodetect_video_codec(self):
    #     autodetected_video_format = self.release_name.video_format
    #     autodetected_source = self.release_name.source

    #     if autodetected_video_format == 'x264':
    #         return 'x264'
    #     elif autodetected_video_format == 'x265':
    #         return 'x265'

    #     elif autodetected_video_format == 'H.264':
    #         return 'H.264'
    #     elif autodetected_video_format == 'H.265':
    #         return 'H.265'

    #     elif autodetected_video_format == 'XviD':
    #         return 'XviD'
    #     elif autodetected_video_format == 'DivX':
    #         return 'DivX'

    #     elif autodetected_source == 'BD25':
    #         return 'BD25'
    #     elif autodetected_source == 'BD50':
    #         return 'BD50'
    #     elif autodetected_source == 'BD66':
    #         return 'BD66'
    #     elif autodetected_source == 'BD100':
    #         return 'BD100'

    #     elif autodetected_source == 'DVD5':
    #         return 'DVD5'
    #     elif autodetected_source == 'DVD9':
    #         return 'DVD9'

    #     else:
    #         self.video_codec_job.text = autodetected_video_format

    # def normalize_video_codec(self, text):
    #     return text.strip()

    # def validate_video_codec(self, text):
    #     if not text:
    #         raise ValueError('You must provide a video codec.')

    # # POST parameter "container" seems to be optional.

    # @functools.cached_property
    # def container_job(self):
    #     return jobs.dialog.TextFieldJob(
    #         name=self.get_job_name('container_codec'),
    #         label='Container',
    #         precondition=self.make_precondition('container_job'),
    #         text=self.autodetect_container,
    #         finish_on_success=True,
    #         normalizer=self.normalize_container,
    #         validator=self.validate_container,
    #         **self.common_job_args(),
    #     )

    # async def autodetect_container(self):
    #     if utils.fs.find_name('BDMV', self.content_path, validator=os.path.isdir):
    #         return 'm2ts'
    #     elif utils.fs.file_extension(self.content_path).lower() == 'iso':
    #         return 'ISO'

    #     info = utils.video.default_track('general', self.content_path, default=None)
    #     if info:
    #         container = info.get('Format')
    #         if container == 'Matroska':
    #             return 'MKV'
    #         elif container == 'MPEG-4':
    #             return 'MP4'
    #         elif container == 'MPEG-TS':
    #             return 'm2ts'
    #         elif container == 'MPEG-PS':
    #             return 'VOB IFO'
    #         elif container == 'AVI':
    #             return 'AVI'
    #         elif container == 'MPEG Video':
    #             return 'MPG'
    #         else:
    #             self.container_job.text = container

    # def normalize_container(self, text):
    #     return text.strip()

    # def validate_container(self, text):
    #     if not text:
    #         raise ValueError('You must provide a container format.')

    # # POST parameter "container" seems to be optional.

    # @functools.cached_property
    # def resolution_job(self):
    #     return jobs.dialog.TextFieldJob(
    #         name=self.get_job_name('resolution_codec'),
    #         label='Resolution',
    #         precondition=self.make_precondition('resolution_job'),
    #         text=self.autodetect_resolution,
    #         finish_on_success=True,
    #         normalizer=self.normalize_resolution,
    #         validator=self.validate_resolution,
    #         **self.common_job_args(),
    #     )

    # _known_resolutions = (
    #     '2160p',
    #     '1080p',
    #     '1080i',
    #     '720p',
    #     '576p',
    #     '480p',
    #     'PAL',
    #     'NTSC',
    # )

    # def autodetect_resolution(self):
    #     dvd_encoding = self.release_name.dvd_encoding
    #     if dvd_encoding:
    #         return dvd_encoding

    #     resolution = utils.video.resolution(self.content_path, default='')
    #     if resolution in self._known_resolutions:
    #         return resolution

    #     # Let the user fix the autodetected resolution
    #     self.resolution_job.text = resolution

    # def normalize_resolution(self, text):
    #     # WIDTHxHEIGHT
    #     match = re.search(r'^\s*(\d*)\s*[xX]\s*(\d*)\s*$', text)
    #     if match:
    #         width = match.group(1)
    #         height = match.group(2)
    #         return f'{width}x{height}'

    #     # 1080p, etc
    #     return text.strip()

    # def validate_resolution(self, text):
    #     if not text:
    #         raise ValueError('You must provide a video resolution.')
    #     elif (
    #             text not in self._known_resolutions
    #             and not re.search(r'^\d+x\d+$', text)
    #     ):
    #         raise ValueError('Invalid resolution')

    @property
    def post_data(self):
        post_data = self._post_data_common

        _log.debug('PTP group ID: %r', self.ptp_group_id)
        if self.ptp_group_id:
            _log.debug('Adding movie format to existing group')
            post_data.update(self._post_data_add_movie_format)
        else:
            _log.debug('Creating new movie group')
            post_data.update(self._post_data_add_new_movie)

        return post_data

    @property
    def _post_data_common(self):
        return {
            **{
                # Feature Film, Miniseries, Short Film, etc
                'type': self.get_job_attribute(self.type_job, 'choice'),

                # Mediainfo and Screenshots
                'release_desc': self.get_job_output(self.description_job, slice=0),

                # Is not main movie (bool)
                'special': '1' if self.options['not_main_movie'] else None,

                # Is personal rip (bool)
                'internalrip': '1' if self.options['personal_rip'] else None,

                # Is scene Release (bool)
                'scene': '1' if self.get_job_attribute(self.scene_check_job, 'is_scene_release') else None,

                # .nfo file content
                'nfo_text': self.read_nfo(),

                # Upload token from staff
                'uploadtoken': self.options.get('upload_token', None),
            },
            **self._post_data_common_source,
            **self._post_data_common_codec,
            **self._post_data_common_container,
            **self._post_data_common_resolution,
            **self._post_data_common_edition,
            **self._post_data_common_subtitles,
            **self._post_data_common_trumpable,
        }

    @property
    def _post_data_common_source(self):
        return {
            'source': 'Other',
            'other_source': self.get_job_output(self.source_job, slice=0),
        }

    @property
    def _post_data_common_codec(self):
        return {
            # Server-side autodetection
            'codec': '* Auto-detect',
            'other_codec': '',

            # # Custom codec
            # 'codec': 'Other',
            # 'other_codec': self.get_job_output(self.video_codec_job, slice=0),
        }

    @property
    def _post_data_common_container(self):
        return {
            # Server-side autodetection
            'container': '* Auto-detect',
            'other_container': ''

            # # Custom container
            # 'container': 'Other',
            # 'other_container': self.get_job_output(self.container_job, slice=0),
        }

    @property
    def _post_data_common_resolution(self):
        return {
            # Server-side autodetection
            'resolution': '* Auto-detect',
            'other_resolution': '',
        }

        # Custom resolution
        # resolution = self.get_job_output(self.resolution_job, slice=0)
        # # WIDTHxHEIGHT
        # if 'x' in resolution:
        #     width, height = resolution.split('x', maxsplit=1)
        #     return {
        #         'resolution': 'Other',  # Custom resolution
        #         'other_resolution_width': width,
        #         'other_resolution_height': height,
        #     }

        # # 1080p, 720p, etc
        # else:
        #     return {
        #         'resolution': resolution,
        #         'other_resolution': releaseInfo.Resolution,
        #     }

    @property
    def _post_data_common_subtitles(self):
        # Translate BCP47 codes into PTP numeric codes from upload.php
        codes = []
        for sub in self.subtitles:
            ptp_code = None

            if ptp_code is None and sub.region and sub.forced:
                # Language, country and "forced" flag, e.g. "pt-BR (forced)"
                ptp_code = metadata.ptp_subtitles.get(f'{sub.language}-{sub.region} (forced)')

            if ptp_code is None and sub.region:
                # Language and "forced" flag, e.g. "pt-BR"
                ptp_code = metadata.ptp_subtitles.get(f'{sub.language}-{sub.region}')

            if ptp_code is None and sub.forced:
                # Language and "forced" flag, e.g. "pt (forced)"
                ptp_code = metadata.ptp_subtitles.get(f'{sub.language} (forced)')

            if ptp_code is None:
                # Language, e.g. "pt"
                ptp_code = metadata.ptp_subtitles.get(sub.language)

            if ptp_code:
                codes.append(ptp_code)

        # Send "No subtitles" if there aren't any or if none of the existing
        # subtitles are supported in metadata.ptp_subtitles, i.e. we couldn't
        # find any `codes`.
        if not codes:
            codes.append(metadata.ptp_subtitles['No Subtitles'])

        _log.debug('PTP subtitle codes: %r', codes)
        return {'subtitles[]': codes}

    @property
    def _post_data_common_edition(self):
        text = self.get_job_output(self.edition_job, slice=0)
        return {
            # Edition Information ("Director's Cut", "Dual Audio", etc.)
            'remaster': 'on' if text else None,
            'remaster_title': text if text else None,
            # 'remaster_year': ...,
            # 'remaster_other_input': ...,
        }

    @property
    def _post_data_common_trumpable(self):
        return {
            'trumpable[]': [
                # Convert pretty strings to API values
                metadata.PtpTrumpableReason.from_string(string).value
                for string in self.trumpable_job.output
            ],
        }

    @property
    def _post_data_add_movie_format(self):
        # Upload another release to existing movie group
        return {
            'groupid': self.ptp_group_id,
        }

    @property
    def _post_data_add_new_movie(self):
        # Upload movie that is not on PTP yet in any format
        post_data = {
            # IMDb ID (must be 7 characters without the leading "tt")
            'imdb': self.tracker.normalize_imdb_id(self.imdb_id),
            # Release year
            'title': self.get_job_output(self.title_job, slice=0),
            # Release year
            'year': self.get_job_output(self.year_job, slice=0),
            # Movie plot or summary
            'album_desc': self.get_job_output(self.plot_job, slice=0),
            # Genre
            'tags': self.get_job_output(self.tags_job, slice=0),
            # Youtube ID
            # 'trailer': ...,
            # Poster URL
            'image': self.get_job_output(self.poster_job, slice=0),
        }

        # TODO: Is this required?
        # # ???: For some reason PtpUploader uses "artist" and "importance" in the
        # #      POST data while the website form uses "artists", "importances"
        # #      and "roles".
        # artists = self.get_job_output(self.artists_job):
        # if artists:
        #     post_data['artist'] = []
        #     post_data['importance'] = []
        #     for name in artists:
        #         # `importance` is the artist type:
        #         # 1: Director
        #         # 2: Writer
        #         # 3: Producer
        #         # 4: Composer
        #         # 5: Actor
        #         # 6: Cinematographer
        #         post_data['importance'].append('1')
        #         post_data['artist'].append(name)
        #         post_data['role'].append(name)

        return post_data
