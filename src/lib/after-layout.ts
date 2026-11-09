/**
 * Runs `read` just after the next frame has been laid out, when reading scroll positions and
 * sizes is free. Reading them straight from an effect during hydration, while the page is still
 * being changed, makes the browser stop and lay it out on the spot (a forced reflow).
 *
 * Returns a function that cancels it.
 */
export function afterLayout(read: () => void): () => void {
	let timer: ReturnType<typeof setTimeout>;
	const frame = requestAnimationFrame(() => {
		timer = setTimeout(read);
	});
	return () => {
		cancelAnimationFrame(frame);
		clearTimeout(timer);
	};
}
