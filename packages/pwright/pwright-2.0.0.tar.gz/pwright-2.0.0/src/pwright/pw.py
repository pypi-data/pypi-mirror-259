from contextlib import contextmanager
import logging
from pathlib import Path
import typing as t

from playwright.sync_api import Browser as Browser
from playwright.sync_api import BrowserContext as BrowserContext
from playwright.sync_api import Dialog as Dialog
from playwright.sync_api import ElementHandle as ElementHandle
from playwright.sync_api import Page as Page
from playwright.sync_api import Playwright as Playwright
from playwright.sync_api import Route as Route
from playwright.sync_api import TimeoutError as TimeoutError
from playwright.sync_api import sync_playwright as playwright

from ._utils import DEFAULT_INIT_SCRIPT
from ._utils import relative_to_cwd


Eh = ElementHandle


logger = logging.getLogger(__name__)


def screenshot(
    page: Page,
    *,
    file=Path.cwd() / '.temp' / 'screenshot.png',
):
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_bytes(page.screenshot())
    logger.info(f' -> screenshot: ./{relative_to_cwd(file)}')


@contextmanager
def pw_page(
    *,
    # [browser]
    timeout: t.Optional[float] = None,
    headed: t.Optional[bool] = None,
    # [context]
    user_agent: t.Optional[str] = None,
    base_url: t.Optional[str] = None,
    # [context.tracing]
    tracing=False,
    screenshots=True,
    snapshots=True,
    sources=True,
    path='trace.zip',
    # [page]
    init_script=DEFAULT_INIT_SCRIPT,
):
    with pw_context(timeout=timeout, headed=headed, user_agent=user_agent, base_url=base_url) as (
        browser,
        context,
    ):
        if tracing:
            context.tracing.start(screenshots=screenshots, snapshots=snapshots, sources=sources)
        with context.new_page() as page:
            page.add_init_script(init_script)
            logger.debug(f'{page = }')
            yield browser, context, page
        if tracing:
            context.tracing.stop(path=path)


@contextmanager
def pw_context(
    *,
    # [browser]
    timeout: t.Optional[float] = None,
    headed: t.Optional[bool] = None,
    # [context]
    user_agent: t.Optional[str] = None,
    base_url: t.Optional[str] = None,
):
    with pw_browser(timeout=timeout, headed=headed) as browser:
        with browser.new_context(user_agent=user_agent, base_url=base_url) as context:
            logger.debug(f'{context = }')
            yield browser, context


@contextmanager
def pw_browser(
    *,
    # [browser]
    timeout: t.Optional[float] = None,
    headed: t.Optional[bool] = None,
):
    # https://playwright.dev/python/docs/test-runners#fixtures
    with playwright() as _playwright:
        logger.debug(f'{_playwright = }')
        with _playwright.chromium.launch(timeout=timeout, headless=not headed) as browser:
            browser_type = browser.browser_type
            logger.debug(f'{browser_type = }')
            logger.debug(f'{browser = }')
            browser_name = browser_type.name
            logger.debug(f'{browser_name = }')
            yield browser


playwright_page = pw_page
playwright_context = pw_context
playwright_browser = pw_browser
