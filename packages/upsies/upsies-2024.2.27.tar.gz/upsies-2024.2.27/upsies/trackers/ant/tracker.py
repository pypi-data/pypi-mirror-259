"""
Concrete :class:`~.base.TrackerBase` subclass for ANT
"""

import urllib

from ... import errors, utils
from ..base import TrackerBase
from .config import AntTrackerConfig
from .jobs import AntTrackerJobs

import logging  # isort:skip
_log = logging.getLogger(__name__)


class AntTracker(TrackerBase):
    name = 'ant'
    label = 'ANT'

    setup_howto_template = (
        '{howto.introduction}\n'
        '\n'
        '{howto.next_section}. API Key\n'
        '\n'
        '   {howto.current_section}.1 On the website, go to USERNAME -> Edit -> Access Settings\n'
        '       and scroll down to "API keys".\n'
        '   {howto.current_section}.2 In the "Create a new Key" row, tick the "Upload" box.\n'
        '   {howto.current_section}.3 Click on "Save profile".\n'
        '   {howto.current_section}.4 Scroll down to "API keys" again and copy the new API_KEY.\n'
        '   {howto.current_section}.5 $ upsies set trackers.{tracker.name}.apikey API_KEY\n'
        '\n'
        '{howto.next_section}. Announce URL\n'
        '\n'
        '   {howto.current_section}.1 On the website, click on "Upload" and copy the ANNOUNCE_URL.\n'
        '   {howto.current_section}.2 $ upsies set trackers.{tracker.name}.announce_url ANNOUNCE_URL\n'
        '\n'
        '{howto.autoseed}\n'
        '\n'
        '{howto.reuse_torrents}\n'
        '\n'
        '{howto.upload}\n'
    )

    TrackerConfig = AntTrackerConfig
    TrackerJobs = AntTrackerJobs

    @property
    def _base_url(self):
        return self.options['base_url']

    @property
    def _api_url(self):
        return urllib.parse.urljoin(self._base_url, '/api.php')

    @property
    def apikey(self):
        apikey = self.options.get('apikey')
        if apikey:
            return apikey
        else:
            raise errors.RequestError('No API key configured')

    async def _login(self):
        pass

    async def _logout(self):
        pass

    async def get_announce_url(self):
        announce_url = self.options.get('announce_url')
        if announce_url:
            return announce_url
        else:
            raise errors.AnnounceUrlNotSetError(tracker=self)

    async def upload(self, tracker_jobs):
        post_data = tracker_jobs.post_data

        _log.debug('POSTing data:')
        for k, v in post_data.items():
            _log.debug(' * %s = %s', k, v)

        post_files = tracker_jobs.post_files
        _log.debug('POSTing files: %r', post_files)

        json = await self._request(
            method='POST',
            url=self._api_url,
            cache=False,
            data=post_data,
            files=post_files,
        )

        if json.get('status') == 'success':
            return tracker_jobs.torrent_filepath
        elif json.get('error'):
            raise errors.RequestError(f'Upload failed: {json["error"]}')
        else:
            raise RuntimeError(f'Unexpected response: {json!r}')

    async def _request(self, method, *args, **kwargs):
        try:
            # `method` is "GET" or "POST"
            response = await getattr(utils.http, method.lower())(
                *args,
                user_agent=True,
                **kwargs,
            )
        except errors.RequestError as e:
            _log.debug(f'Request failed: {e!r}')
            _log.debug(f'url={e.url!r}')
            _log.debug(f'text={e.text!r}')
            _log.debug(f'headers={e.headers!r}')
            _log.debug(f'status_code={e.status_code!r}')
            # The error message in the HTTP response is JSON. Try to parse that
            # to get the actual error message. If that fails, raise the
            # RequestError as is.
            json = e.json(default=None)
            if json:
                _log.debug('ERROR IS JSON: %r', json)
                return json
            else:
                _log.debug('Response is not JSON: %r', e.text)
                raise RuntimeError(f'Unexpected response: {e!r}')
        else:
            _log.debug('RESPONSE: %r', response)
            json = response.json()
        return json
