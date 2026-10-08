<script lang="ts">
	// Floating glass button: the ring fills as you read down the page, a tap goes back to the top.
	// It appears once the hero is behind you.
	const CIRCUMFERENCE = 2 * Math.PI * 21;

	let progress = $state(0);
	let visible = $state(false);

	$effect(() => {
		let frame = 0;
		const update = () => {
			frame = 0;
			const max = document.documentElement.scrollHeight - window.innerHeight;
			progress = max > 0 ? Math.min(1, window.scrollY / max) : 0;
			visible = window.scrollY > window.innerHeight * 0.8;
		};
		const schedule = () => {
			if (!frame) frame = requestAnimationFrame(update);
		};
		update();
		window.addEventListener('scroll', schedule, { passive: true });
		window.addEventListener('resize', schedule);
		return () => {
			cancelAnimationFrame(frame);
			window.removeEventListener('scroll', schedule);
			window.removeEventListener('resize', schedule);
		};
	});

	function toTop() {
		const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
	}
</script>

<button
	type="button"
	class="scroll-top glass"
	class:visible
	onclick={toTop}
	aria-label="Back to top ({Math.round(progress * 100)}% read)"
	aria-hidden={!visible}
	tabindex={visible ? 0 : -1}
>
	<svg class="ring" viewBox="0 0 48 48" aria-hidden="true">
		<circle class="ring-track" cx="24" cy="24" r="21" />
		<circle
			class="ring-bar"
			cx="24"
			cy="24"
			r="21"
			stroke-dasharray={CIRCUMFERENCE}
			stroke-dashoffset={CIRCUMFERENCE * (1 - progress)}
		/>
	</svg>
	<svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
		<polyline points="18 15 12 9 6 15"></polyline>
	</svg>
</button>

<style>
	.scroll-top {
		position: fixed;
		right: max(1rem, env(safe-area-inset-right));
		bottom: max(1.25rem, env(safe-area-inset-bottom));
		z-index: 900;
		display: grid;
		place-items: center;
		width: 52px;
		height: 52px;
		border: none;
		border-radius: 50%;
		color: var(--tint);
		cursor: pointer;
		opacity: 0;
		translate: 0 14px;
		scale: 0.85;
		pointer-events: none;
		transition:
			opacity 0.3s ease,
			translate 0.45s var(--ease-spring),
			scale 0.45s var(--ease-spring);
	}

	.scroll-top.visible {
		opacity: 1;
		translate: 0 0;
		scale: 1;
		pointer-events: auto;
	}

	.scroll-top:active {
		scale: 0.92;
	}

	.ring,
	.arrow {
		grid-area: 1 / 1;
	}

	.ring {
		width: 100%;
		height: 100%;
		rotate: -90deg;
	}

	.ring-track,
	.ring-bar {
		fill: none;
		stroke-width: 2.5;
	}

	.ring-track {
		stroke: rgba(0, 56, 138, 0.12);
	}

	.ring-bar {
		stroke: var(--tint);
		stroke-linecap: round;
	}
</style>
