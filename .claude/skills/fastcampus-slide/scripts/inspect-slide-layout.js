/* Paste into a browser evaluate tool after animations finish. Read-only; no dependencies.
   Captures the active slide's layout, missing images, and interaction state.
   This does not prove that the teaching message or visual composition is correct. */
(() => {
  const slide = document.querySelector('.slide.active');
  if (!slide) return { error: '활성 슬라이드가 없습니다.' };
  const body = slide.querySelector('.slide__body');
  if (!body) return { error: 'slide__body가 없습니다.' };
  const bounds = body.getBoundingClientRect();
  const visible = e => {
    const style = getComputedStyle(e);
    return style.display !== 'none' && style.visibility !== 'hidden' &&
      !e.closest('[aria-hidden="true"], [hidden]');
  };
  const overflow = [...body.querySelectorAll('*')]
    .filter(e => e.namespaceURI === 'http://www.w3.org/1999/xhtml' && visible(e))
    .flatMap(e => {
      const r = e.getBoundingClientRect();
      if (!r.width || !r.height) return [];
      const edges = [r.left < bounds.left - 2 && 'left', r.right > bounds.right + 2 && 'right',
        r.top < bounds.top - 2 && 'top', r.bottom > bounds.bottom + 2 && 'bottom'].filter(Boolean);
      return edges.length ? [{ tag: e.tagName, class: e.className,
        text: e.textContent.trim().slice(0, 90), edges }] : [];
    });
  return {
    title: slide.querySelector('.slide__title')?.textContent.trim(),
    pattern: slide.dataset.pattern ?? slide.dataset.visual,
    viewport: { width: innerWidth, height: innerHeight },
    body: { width: bounds.width, height: bounds.height },
    overflow,
    brokenImages: [...slide.querySelectorAll('img')].filter(e => !e.complete || !e.naturalWidth).map(e => e.src),
    animationGroups: [...slide.querySelectorAll('.anim-item')].map(e => ({
      class: e.className.baseVal ?? e.className, step: e.dataset.animStep,
      animation: getComputedStyle(e).animationName, delay: getComputedStyle(e).animationDelay
    })),
    tabs: [...slide.querySelectorAll('[role="tab"]')].map(e => ({
      label: e.textContent.trim(), selected: e.getAttribute('aria-selected')
    })),
    reducedMotion: matchMedia('(prefers-reduced-motion: reduce)').matches
  };
})();
