<script lang="ts" module>
	// The intro plays on a full page load. Coming back to / through client-side navigation
	// (e.g. from /privacy) skips it.
	let introPlayed = false;
</script>

<script lang="ts">
	import { browser } from '$app/environment';
	import { clickSpring } from '$lib/attachments/click-spring';
	import { INSTAGRAM_URL } from '$lib/site';
	// Inlined at build time: the intro never waits on a download, cold cache or not
	import plateSvg from '$lib/assets/brand/plate-lot7.svg?raw';

	const skipIntro = browser && introPlayed;
	if (browser) introPlayed = true;

	let section: HTMLElement;
	let video: HTMLVideoElement;
	let paused = $state(true);
	// Set when the visitor pauses (or prefers no motion) so we never resume on our own
	let userPaused = false;

	$effect(() => {
		const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		const connection = (
			navigator as Navigator & { connection?: { saveData?: boolean; effectiveType?: string } }
		).connection;
		const saveData = connection?.saveData === true;
		// The video is 2–3 MB: on 2G/3G the 66 KB poster is the page, and the play button stays
		const slowNetwork = ['slow-2g', '2g', '3g'].includes(connection?.effectiveType ?? '');

		// Poster + play button only; with preload="none" the video is never downloaded
		if (reduceMotion || saveData || slowNetwork) {
			userPaused = true;
			return;
		}

		// Only play while the video is on screen
		const observer = new IntersectionObserver(
			([entry]) => {
				if (entry.isIntersecting && !userPaused) video.play().catch(() => {});
				else if (!entry.isIntersecting) video.pause();
			},
			{ threshold: 0.25 }
		);
		observer.observe(video);
		return () => observer.disconnect();
	});

	// Any tap, key, scroll or wheel jumps the intro to its end state
	$effect(() => {
		if (skipIntro) return;
		const events = ['pointerdown', 'keydown', 'wheel', 'touchstart'] as const;
		const stop = () => events.forEach((type) => window.removeEventListener(type, finish));
		function finish() {
			for (const animation of section.getAnimations({ subtree: true })) {
				if (animation instanceof CSSAnimation && animation.animationName.includes('intro-')) {
					animation.finish();
				}
			}
			stop();
		}
		events.forEach((type) => window.addEventListener(type, finish, { passive: true }));
		const timer = setTimeout(stop, 5000);
		return () => {
			clearTimeout(timer);
			stop();
		};
	});

	function togglePlayback() {
		if (video.paused) {
			userPaused = false;
			video.play().catch(() => {});
		} else {
			userPaused = true;
			video.pause();
		}
	}
</script>

<svelte:head>
	<!-- The poster is what the plate opens onto: fetch it first so the reveal never shows an empty frame -->
	<link rel="preload" as="image" href="/videos/lot7-showcase-poster.webp" fetchpriority="high" />
</svelte:head>

<section class="hero-section" class:intro-played={skipIntro} id="hero" bind:this={section}>
	<div class="hero-inner container">
		<h1 class="visually-hidden">Lot 7 Cafe — specialty coffee and vinyl listening room in Naga City</h1>

		<!-- Main Visual: Dynamic Showcase Video (4:5 Portrait on mobile, 16:9 Landscape on desktop).
		     The stage is a size container so the intro can line the plate up with the video frame. -->
		<div class="showcase-stage">
			<div class="showcase-video-wrapper photo-frame">
				<!-- Playback is started from script (not `autoplay`) so reduced-motion and
				     data-saver visitors get the poster only. The on-screen text is repeated
				     in the manifesto section, so the video itself is hidden from screen readers. -->
				<video
					bind:this={video}
					poster="/videos/lot7-showcase-poster.webp"
					preload="none"
					loop
					muted
					playsinline
					aria-hidden="true"
					class="showcase-video"
					onplay={() => (paused = false)}
					onpause={() => (paused = true)}
				>
					<!-- AV1 is ~40% smaller; browsers without AV1 decode fall through to H.264 -->
					<source src="/videos/lot7-showcase-av1.mp4" type={'video/mp4; codecs="av01.0.05M.08"'} />
					<source src="/videos/lot7-showcase.mp4" type={'video/mp4; codecs="avc1.64001F"'} />
				</video>

				<button
					type="button"
					class="video-toggle"
					onclick={togglePlayback}
					aria-label={paused ? 'Play background video' : 'Pause background video'}
				>
					{#if paused}
						<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
							<path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"></path>
						</svg>
					{:else}
						<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
							<rect x="6" y="5" width="4" height="14" rx="1"></rect>
							<rect x="14" y="5" width="4" height="14" rx="1"></rect>
						</svg>
					{/if}
				</button>
			</div>

			<!-- Intro: the LOT 7 plate from the wall drops in, then opens into the video frame -->
			<div class="intro-plate" aria-hidden="true">{@html plateSvg}</div>
		</div>

		<!-- Main tagline, set in the official signage artwork (design-assets/LOGOS/SIGNAGE.png) -->
		<div class="hero-caption-block">
			<p class="hero-creed">
				<enhanced:img
					src="$lib/assets/brand/tagline-serif.png"
					alt="your neighborhood, just a little better."
					width="640"
					class="hero-tagline-art"
				/>
			</p>
		</div>

		<!-- Fat Seed Inspired Bottom In-Page Navigation Pills Dock -->
		<nav class="hero-pills-dock font-mono" aria-label="Hero quick jump">
			<a href="#story" class="hero-pill" style="--i: 0">
				<span>THE STORY</span>
			</a>
			<a href="#room" class="hero-pill" style="--i: 1">
				<span>THE ROOM</span>
			</a>
			<a href="#menu" class="hero-pill" style="--i: 2">
				<span>MENU</span>
			</a>
			<a href="#sound" class="hero-pill" style="--i: 3">
				<span>SOUND</span>
			</a>
			<a href="#visit" class="hero-pill" style="--i: 4">
				<span>VISIT US</span>
			</a>
			<a 
				href={INSTAGRAM_URL} 
				target="_blank" 
				rel="noopener noreferrer" 
				class="hero-pill hero-pill-accent"
				style="--i: 5"
				{@attach clickSpring}
				aria-label="@LOT7.CAFE on Instagram"
			>
				<svg class="ig-svg-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
					<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
					<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
				</svg>
				<span>@LOT7.CAFE</span>
			</a>
		</nav>
	</div>
</section>

<style>
	.hero-section {
		height: calc(100dvh - var(--header-height));
		min-height: 580px;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 0.5rem 0 1.5rem;
		box-sizing: border-box;
		position: relative;
		/* Sideways only: the intro plate falls in from above the screen, behind the glass header */
		overflow-x: clip;
	}

	.hero-inner {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-evenly;
		text-align: center;
		gap: 1.25rem;
		width: 100%;
		height: 100%;
	}

	/* Dynamic Showcase Video Player (Desktop 16:9) */
	.showcase-stage {
		/* Plate size in the stage's own units: 2:1, never taller than the frame */
		--plate-w: min(64cqw, 108cqh);
		/* The plate art is 220 x 112 (face plus its drop edge) */
		--plate-h: calc(var(--plate-w) * 0.509);
		--morph-ease: cubic-bezier(0.32, 0.72, 0, 1);
		--morph-at: 1.6s;
		--morph-for: 1.5s;
		width: min(92vw, 1150px);
		max-height: calc(75dvh - 5.5rem);
		aspect-ratio: 16 / 9;
		position: relative;
		container-type: size;
	}

	.showcase-video-wrapper {
		position: absolute;
		inset: 0;
		overflow: hidden;
		background: #000000;
		border-radius: var(--radius-card);
		box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06), 0 24px 60px rgba(0, 0, 0, 0.14);
	}

	.showcase-video {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
	}

	/* Pause / play control (WCAG 2.2.2: moving content longer than 5s must be pausable) */
	.video-toggle {
		position: absolute;
		right: 0.9rem;
		bottom: 0.9rem;
		z-index: 2;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 44px;
		height: 44px;
		border-radius: 50%;
		border: none;
		background: var(--glass-dark-bg);
		-webkit-backdrop-filter: var(--glass-blur);
		backdrop-filter: var(--glass-blur);
		box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.25), inset 0 0 0 0.5px rgba(255, 255, 255, 0.3);
		color: #ffffff;
		cursor: pointer;
		transition: transform 0.2s var(--ease-out);
	}

	.video-toggle:active {
		transform: scale(0.9);
	}

	/* Ring sits over the (usually dark) video */
	.video-toggle:focus-visible {
		outline-color: #ffffff;
	}

	.hero-caption-block {
		display: flex;
		flex-direction: column;
		align-items: center;
		max-width: 820px;
	}

	.hero-creed {
		margin: 0;
		line-height: 0;
	}

	.hero-creed :global(.hero-tagline-art) {
		display: block;
		height: clamp(64px, 9vh, 100px);
		width: auto;
		user-select: none;
		-webkit-user-drag: none;
	}

	/* Fat Seed Inspired Interactive Pills Dock */
	.hero-pills-dock {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		gap: 0.65rem;
		width: 100%;
		max-width: 850px;
	}

	/* Glass capsules floating on the canvas */
	.hero-pill {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		min-height: 40px;
		padding: 0.5rem 1.15rem;
		border-radius: var(--radius-pill);
		background: var(--glass-bg);
		-webkit-backdrop-filter: var(--glass-blur);
		backdrop-filter: var(--glass-blur);
		box-shadow: var(--glass-edge), 0 1px 2px rgba(0, 0, 0, 0.05), 0 6px 18px rgba(0, 0, 0, 0.06);
		color: var(--text-main);
		font-size: 0.72rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		text-decoration: none;
		user-select: none;
		transition: transform 0.2s var(--ease-out), background-color 0.15s ease, color 0.15s ease;
		white-space: nowrap;
	}

	.hero-pill:hover {
		background: #ffffff;
		color: var(--tint);
	}

	.hero-pill:active {
		transform: scale(0.95);
	}

	.hero-pill.hero-pill-accent {
		gap: 0.4rem;
		background: var(--tint);
		color: #ffffff;
		box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08), 0 6px 18px rgba(0, 56, 138, 0.25);
	}

	.hero-pill.hero-pill-accent :global(.ig-svg-icon) {
		flex-shrink: 0;
	}

	.hero-pill.hero-pill-accent:hover {
		background: var(--tint-pressed);
		color: #ffffff;
	}

	/* =========================================
	   INTRO: THE PLATE DROP (about 3.7s, plain CSS so it runs while scripts load)
	   0.15s  the LOT 7 plate falls in and lands with a spring and a swing
	   1.0s   a glint runs across the embossed letters
	   1.6s   the morph, 1.5s: the plate's box grows into the video frame while the frame's
	          clip grows in step (same curve, same timing, so their edges always meet). The
	          lettering dissolves into a brand-blue slab, which then clears to the footage.
	   2.8s   the tagline is written in; 3.0s the pills rise one by one
	   The plate art is inlined and the poster preloaded, so nothing here waits on the network;
	   html.intro-hold (set in app.html) pauses it all while the page loads in a background tab.
	   ========================================= */
	.intro-plate {
		position: absolute;
		left: 50%;
		top: 50%;
		z-index: 3;
		width: var(--plate-w);
		height: var(--plate-h);
		translate: -50% -50%;
		/* Matches the plate's corner (rx 10 on a 220-wide face) */
		border-radius: calc(var(--plate-w) * 0.045);
		background-color: transparent;
		pointer-events: none;
		overflow: hidden;
	}

	.intro-plate :global(svg) {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		display: block;
	}

	/* The glint */
	.intro-plate::after {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(105deg, transparent 38%, rgba(255, 255, 255, 0.6) 50%, transparent 62%) no-repeat;
		background-size: 250% 100%;
		background-position: 130% 0;
		opacity: 0;
	}

	.hero-section.intro-played .intro-plate {
		display: none;
	}

	.hero-section:not(.intro-played) .intro-plate {
		animation:
			intro-drop 0.95s 0.15s both,
			intro-grow var(--morph-for) var(--morph-ease) var(--morph-at) forwards,
			intro-clear var(--morph-for) linear var(--morph-at) forwards;
	}

	.hero-section:not(.intro-played) .intro-plate :global(svg) {
		animation: intro-art-fade calc(var(--morph-for) * 0.45) ease-in var(--morph-at) forwards;
	}

	.hero-section:not(.intro-played) .intro-plate::after {
		animation: intro-glint 0.7s ease-in-out 1s both;
	}

	.hero-section:not(.intro-played) .showcase-video-wrapper {
		animation:
			intro-show 1ms var(--morph-at) backwards,
			intro-open var(--morph-for) var(--morph-ease) var(--morph-at) backwards,
			intro-shadow 0.6s ease calc(var(--morph-at) + var(--morph-for)) backwards;
	}

	.hero-section:not(.intro-played) .showcase-video {
		animation: intro-settle calc(var(--morph-for) + 0.4s) var(--morph-ease) var(--morph-at) backwards;
	}

	.hero-section:not(.intro-played) .video-toggle {
		animation: intro-fade 0.4s ease 3.1s backwards;
	}

	.hero-section:not(.intro-played) .hero-creed {
		animation: intro-write 0.9s cubic-bezier(0.22, 1, 0.36, 1) 2.8s backwards;
	}

	.hero-section:not(.intro-played) .hero-pill {
		animation: intro-rise 0.7s var(--ease-spring) backwards;
		animation-delay: calc(3s + var(--i, 0) * 70ms);
	}

	/* Page opened in a background tab: wait until it's actually on screen */
	:global(html.intro-hold) .hero-section :global(*),
	:global(html.intro-hold) .hero-section :global(*::after) {
		animation-play-state: paused !important;
	}

	@keyframes intro-drop {
		0% {
			transform: translateY(-110vh) rotate(-9deg);
			filter: drop-shadow(0 50px 40px rgba(0, 0, 0, 0));
			animation-timing-function: cubic-bezier(0.55, 0, 0.85, 0.35);
		}
		55% {
			transform: translateY(2.5%) rotate(2.5deg);
			animation-timing-function: ease-out;
		}
		70% {
			transform: translateY(-1.5%) rotate(-1.2deg);
			animation-timing-function: ease-in-out;
		}
		85% {
			transform: translateY(0.5%) rotate(0.4deg);
			animation-timing-function: ease-in-out;
		}
		100% {
			transform: none;
			filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0.28));
		}
	}

	@keyframes intro-glint {
		0% {
			opacity: 0;
			background-position: 130% 0;
		}
		30% {
			opacity: 1;
		}
		100% {
			opacity: 0;
			background-position: -30% 0;
		}
	}

	/* The plate's box becomes the frame */
	@keyframes intro-grow {
		to {
			width: 100cqw;
			height: 100cqh;
			border-radius: var(--radius-card);
		}
	}

	/* Brand-blue slab: fills in behind the dissolving lettering, then clears to the footage,
	   catching a glass highlight on the way; the landing shadow fades as it becomes the frame */
	@keyframes intro-clear {
		0% {
			background-color: rgba(0, 56, 138, 0);
			box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0);
			filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0.28));
		}
		15% {
			background-color: rgba(0, 56, 138, 1);
			box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45);
		}
		100% {
			background-color: rgba(0, 56, 138, 0);
			box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0);
			filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0));
			/* Done: take the now-empty box out of the way entirely */
			visibility: hidden;
		}
	}

	@keyframes intro-art-fade {
		to {
			opacity: 0;
			transform: scale(1.04);
		}
	}

	/* The frame waits, hidden, until the plate has landed */
	@keyframes intro-show {
		from {
			opacity: 0;
		}
	}

	/* ...then grows out of the plate's exact outline, centred in the stage */
	@keyframes intro-open {
		from {
			clip-path: inset(
				calc((100cqh - var(--plate-h)) / 2) calc((100cqw - var(--plate-w)) / 2)
					round calc(var(--plate-w) * 0.045)
			);
		}
		to {
			clip-path: inset(0 round var(--radius-card));
		}
	}

	/* The clip hides the frame's shadow while it opens; bring it in once the frame is whole */
	@keyframes intro-shadow {
		from {
			box-shadow: none;
		}
	}

	@keyframes intro-settle {
		from {
			transform: scale(1.2);
		}
	}

	@keyframes intro-fade {
		from {
			opacity: 0;
		}
	}

	@keyframes intro-write {
		from {
			clip-path: inset(0 100% 0 0);
			transform: translateY(6px);
		}
		to {
			clip-path: inset(0 0 0 0);
			transform: none;
		}
	}

	@keyframes intro-rise {
		from {
			opacity: 0;
			transform: translateY(14px) scale(0.96);
		}
	}

	/* No intro at all for visitors who ask for less motion (the global rule only shortens
	   durations, which would still leave everything waiting out its delay) */
	@media (prefers-reduced-motion: reduce) {
		.intro-plate {
			display: none;
		}

		.hero-section .showcase-video-wrapper,
		.hero-section .showcase-video,
		.hero-section .video-toggle,
		.hero-section .hero-creed,
		.hero-section .hero-pill {
			animation: none !important;
		}
	}

	/* Mobile View (Matching Fat Seed Portrait Energy) */
	@media (max-width: 768px) {
		.hero-section {
			height: calc(100dvh - var(--header-height));
			min-height: calc(100dvh - var(--header-height));
			padding: 0.75rem var(--page-padding) 1.25rem;
		}

		.hero-inner {
			justify-content: space-evenly;
			gap: 0.5rem;
			height: 100%;
		}

		/* 4:5 Vertical Portrait Video on Phone */
		.showcase-stage {
			--plate-w: min(88cqw, 108cqh);
			width: min(88vw, 360px);
			height: min(48dvh, 420px);
			max-height: none;
			aspect-ratio: 4 / 5;
		}

		.hero-creed :global(.hero-tagline-art) {
			height: clamp(56px, 8vh, 72px);
		}

		/* Centered Ergonomic Dock on Mobile */
		.hero-pills-dock {
			display: flex;
			flex-wrap: wrap;
			justify-content: center;
			gap: 0.45rem;
			width: 100%;
			max-width: 380px;
		}

		.hero-pill {
			padding: 0.45rem 0.75rem;
			font-size: 0.7rem;
			letter-spacing: 0.04em;
			text-align: center;
		}
	}
</style>
