import type { Attachment } from 'svelte/attachments';

/**
 * Plays the spring "bounce" click feedback (keyframes in app.css) each time the element is clicked.
 *
 * Usage: <a href="…" {@attach clickSpring}>
 */
export const clickSpring: Attachment<HTMLElement> = (node) => {
	const restart = () => {
		node.classList.remove('is-springing');
		void node.offsetWidth; // force a reflow so rapid clicks restart the animation
		node.classList.add('is-springing');
	};

	const done = (e: AnimationEvent) => {
		if (e.target === node) node.classList.remove('is-springing');
	};

	node.addEventListener('click', restart);
	node.addEventListener('animationend', done);

	return () => {
		node.removeEventListener('click', restart);
		node.removeEventListener('animationend', done);
	};
};
