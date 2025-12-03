// script.js - Refactored

document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Smooth Scrolling Functionality ---
    // Attach smooth-scroll to internal anchors with a real target (ignore hashes like "#" or "")
    const internalAnchors = Array.from(document.querySelectorAll('a[href^="#"]'))
        .filter(a => {
            const href = a.getAttribute('href');
            return href && href.length > 1; // Exclude '#' and empty hashes
        });

    internalAnchors.forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            const targetEl = document.querySelector(targetId);
            if (!targetEl) return; // Let default behavior happen if no target

            e.preventDefault();
            targetEl.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // --- 3. Generalized File Download Handler ---
    // Supports elements with:
    // - `data-download-src` (path to file)
    // - class `.download-btn` with `data-download-src`
    // - anchors whose id starts with `download-` (legacy support)
    // The element may also provide `data-download-name` to suggest a filename.
    const downloadSelectors = '[data-download-src], .download-btn, a[id^="download-"]';
    const downloadEls = Array.from(document.querySelectorAll(downloadSelectors));

    function handleDownloadClick(e, el) {
        // Prefer explicit data-download-src, then href for anchors
        const src = el.dataset.downloadSrc || el.getAttribute('href');
        if (!src || src.trim() === '' || src.trim().startsWith('#')) {
            // no valid source; nothing to do
            return;
        }

        // Suggested filename from data attribute, otherwise derive from path
        const suggested = el.dataset.downloadName || src.split('/').pop() || 'download.bin';

        // If this is an anchor and it already points to a file, add download attr and let browser handle it
        if (el.tagName.toLowerCase() === 'a') {
            if (!el.hasAttribute('download')) el.setAttribute('download', suggested);
            // let default navigation/download proceed
            return;
        }

        // Otherwise, prevent default and programmatically trigger
        e.preventDefault();
        const a = document.createElement('a');
        a.href = src;
        a.download = suggested;
        document.body.appendChild(a);
        a.click();
        a.remove();
    }

    downloadEls.forEach(el => {
        el.addEventListener('click', (e) => handleDownloadClick(e, el));
    });
});