import datetime
import zoneinfo

from localstack_christmas_countdown.models.timeleft_combined import TimeleftCombined  # noqa: E501
from localstack_christmas_countdown.models.timeleft_period import TimeleftPeriod  # noqa: E501
from localstack_christmas_countdown.models.total_timeleft import TotalTimeleft  # noqa: E501


def timeleft_get(timezone=None):  # noqa: E501
    """Get the time left in sleeps/days etc, combined into one response

    The same as &#x60;/timeleft/{period}&#x60; but all &#x60;period&#x60;s are combined. # noqa: E501

    :param timezone: The timezone
    :type timezone: str

    :rtype: Union[TimeleftCombined, Tuple[TimeleftCombined, int], Tuple[TimeleftCombined, int, Dict[str, str]]
    """
    if not timezone:
        timezone = "Europe/Vienna"
    tz = zoneinfo.ZoneInfo(key=timezone)
    christmas = datetime.datetime(2022, 12, 25, 00, 00, tzinfo=tz)
    now = datetime.datetime.now(tz=tz)
    time_left = christmas - now
    seconds = int(time_left.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    sleeps = days + 1
    weeks = days // 7
    months = christmas.month - now.month
    return TimeleftCombined(
        months=months,
        weeks=weeks,
        sleeps=sleeps,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )


def timeleft_period_get(period, timezone=None):  # noqa: E501
    """Get the time left in sleeps/days etc

     # noqa: E501

    :param period: days/sleeps etc
    :type period: str
    :param timezone: The timezone
    :type timezone: str

    :rtype: Union[TimeleftPeriod, Tuple[TimeleftPeriod, int], Tuple[TimeleftPeriod, int, Dict[str, str]]
    """
    timeleft: TimeleftCombined = timeleft_get(timezone)
    if not hasattr(timeleft, f"_{period}"):
        return 400
    return {period: getattr(timeleft, f"_{period}")}


def timeleft_total_get(timezone=None):  # noqa: E501
    """Get the combined total time left until Christmas

     # noqa: E501

    :param timezone: The timezone
    :type timezone: str

    :rtype: Union[TotalTimeleft, Tuple[TotalTimeleft, int], Tuple[TotalTimeleft, int, Dict[str, str]]
    """
    if not timezone:
        timezone = "Europe/Vienna"
    tz = zoneinfo.ZoneInfo(key=timezone)
    christmas = datetime.datetime(2022, 12, 25, 00, 00, tzinfo=tz)
    now = datetime.datetime.now(tz=tz)
    time_left = christmas - now
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds - (hours * 3600)) // 60
    seconds = time_left.seconds - (minutes * 60 + hours * 3600)
    return TotalTimeleft(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )


def weekday_get(timezone=None):  # noqa: E501
    """Get the day of the week that Christmas Day is on

    The day is a number between 0 and 6, starting with **0 as Sunday**.  You need to convert this number to a day name yourself, either: 1. using a simple array    &#x60;&#x60;&#x60;js    const days &#x3D; [&#39;Sunday&#39;, &#39;Monday&#39;, &#39;Tuesday&#39;, &#39;Wednesday&#39;, &#39;Thursday&#39;, &#39;Friday&#39;, &#39;Saturday&#39;];    console.log(days[6]); // &#x3D;&gt; \&quot;Saturday\&quot;    &#x60;&#x60;&#x60; 2. using built-in methods    &#x60;&#x60;&#x60;js    const i18n &#x3D; new Intl.DateTimeFormat(&#39;en-GB&#39;, { weekday: &#39;long&#39; });    console.log(i18n.format(6)); // &#x3D;&gt; \&quot;Saturday\&quot;    &#x60;&#x60;&#x60; # noqa: E501

    :param timezone: The timezone
    :type timezone: str

    :rtype: Union[float, Tuple[float, int], Tuple[float, int, Dict[str, str]]
    """
    if not timezone:
        timezone = "Europe/Vienna"
    tz = zoneinfo.ZoneInfo(key=timezone)
    christmas = datetime.datetime(2022, 12, 24, 00, 00, tzinfo=tz)
    return christmas.weekday() + 1 % 7
