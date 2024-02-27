import re
from unittest.mock import Mock

import pytest

from upsies import errors
from upsies.trackers.ant import AntTracker, AntTrackerConfig, AntTrackerJobs


@pytest.fixture
def make_tracker():
    def make_tracker(options={}):
        options_ = {
            'username': 'bunny',
            'password': 'hunter2',
            'base_url': 'http://ant.local',
        }
        options_.update(options)
        return AntTracker(options=options_)

    return make_tracker


@pytest.fixture
def tracker(make_tracker):
    return make_tracker()


def test_name_attribute():
    assert AntTracker.name == 'ant'


def test_label_attribute():
    assert AntTracker.label == 'ANT'


def test_TrackerConfig_attribute():
    assert AntTracker.TrackerConfig is AntTrackerConfig


def test_TrackerJobs_attribute():
    assert AntTracker.TrackerJobs is AntTrackerJobs


def test_base_url_attribute(make_tracker):
    tracker = make_tracker(options={'base_url': 'http://foo.local'})
    assert tracker._base_url == 'http://foo.local'


def test_api_url_attribute(make_tracker):
    tracker = make_tracker(options={'base_url': 'http://foo.local'})
    assert tracker._api_url == 'http://foo.local/api.php'


@pytest.mark.parametrize(
    argnames='options, exp_result',
    argvalues=(
        ({}, errors.RequestError('No API key configured')),
        ({'apikey': ''}, errors.RequestError('No API key configured')),
        ({'apikey': 'd34db33f'}, 'd34db33f'),
    ),
    ids=lambda v: repr(v),
)
def test_apikey_attribute(options, exp_result, make_tracker):
    tracker = make_tracker(options=options)
    if isinstance(exp_result, Exception):
        with pytest.raises(type(exp_result), match=rf'^{re.escape(str(exp_result))}$'):
            tracker.apikey
    else:
        assert tracker.apikey == exp_result


@pytest.mark.asyncio
async def test_login(make_tracker):
    tracker = make_tracker()
    return_value = await tracker._login()
    assert return_value is None


@pytest.mark.asyncio
async def test_logout(make_tracker):
    tracker = make_tracker()
    return_value = await tracker._logout()
    assert return_value is None


@pytest.mark.parametrize(
    argnames='options, exp_result',
    argvalues=(
        ({}, errors.AnnounceUrlNotSetError(tracker=Mock())),
        ({'announce_url': ''}, errors.AnnounceUrlNotSetError(tracker=Mock())),
        ({'announce_url': 'http://mock.tracker/annnounce'}, 'http://mock.tracker/annnounce'),
    ),
    ids=lambda v: repr(v),
)
@pytest.mark.asyncio
async def test_get_announce_url(options, exp_result, make_tracker):
    tracker = make_tracker(options=options)
    if isinstance(exp_result, Exception):
        with pytest.raises(type(exp_result), match=rf'^{re.escape(str(exp_result))}$') as exc_info:
            await tracker.get_announce_url()
        assert exc_info.value.tracker == tracker
    else:
        return_value = await tracker.get_announce_url()
        assert return_value == exp_result

    async def get_announce_url(self):
        announce_url = self.options.get('announce_url')
        if announce_url:
            return announce_url
        else:
            raise errors.AnnounceUrlNotSetError(tracker=self)
