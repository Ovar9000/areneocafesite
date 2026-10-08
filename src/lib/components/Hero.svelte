<script lang="ts" module>
	// The intro plays on a full page load. Coming back to / through client-side navigation
	// (e.g. from /privacy) skips it.
	let introPlayed = false;
</script>

<script lang="ts">
	import { browser } from '$app/environment';
	import { clickSpring } from '$lib/attachments/click-spring';
	import { INSTAGRAM_URL } from '$lib/site';

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
	<!-- The poster is what the intro opens onto: fetch it first so the reveal never shows an empty frame -->
	<link rel="preload" as="image" href="/videos/lot7-showcase-poster.webp" fetchpriority="high" />
</svelte:head>

<section class="hero-section" class:intro-played={skipIntro} id="hero" bind:this={section}>
	<div class="hero-inner container">
		<h1 class="visually-hidden">Lot 7 Cafe — specialty coffee and vinyl listening room in Naga City</h1>

		<!-- Main Visual: Dynamic Showcase Video (4:5 Portrait on mobile, 16:9 Landscape on desktop) -->
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
		--intro-ease: cubic-bezier(0.32, 0.72, 0, 1);
		/* Slow to start, so the frost is seen before it clears */
		--defrost-ease: cubic-bezier(0.55, 0, 0.3, 1);
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
		width: min(92vw, 1150px);
		max-height: calc(75dvh - 5.5rem);
		aspect-ratio: 16 / 9;
		position: relative;
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

	/* The pills are the section nav on phones and tablets, where the header collapses to a
	   menu button. From 900px the header shows every section, so they would only repeat it. */
	@media (min-width: 900px) {
		.hero-pills-dock {
			display: none;
		}
	}

	.hero-pill.hero-pill-accent :global(.ig-svg-icon) {
		flex-shrink: 0;
	}

	.hero-pill.hero-pill-accent:hover {
		background: var(--tint-pressed);
		color: #ffffff;
	}

	/* =========================================
	   INTRO: THE FROSTED REVEAL (about 2.8s, plain CSS so it runs while scripts load)
	   0.15s  the frame opens out of a smaller pane of frosted glass
	   0.35s  after a beat, the frost clears over 1.8s: the milky tint lifts, the blur melts
	          and the footage settles from a slight zoom
	   1.3s   a highlight runs once across the clearing glass
	   1.7s   the tagline is written in; 1.85s the pills rise one by one
	   The poster is preloaded, so nothing here waits on the network;
	   html.intro-hold (set in app.html) pauses it all while the page loads in a background tab.
	   ========================================= */
	.showcase-video-wrapper::before,
	.showcase-video-wrapper::after {
		content: '';
		position: absolute;
		inset: 0;
		z-index: 1;
		pointer-events: none;
		opacity: 0;
	}

	/* The frost: a milky white tint over the blurred footage */
	.showcase-video-wrapper::before {
		background: linear-gradient(160deg, rgba(255, 255, 255, 0.5), rgba(235, 240, 250, 0.32));
	}

	/* The highlight */
	.showcase-video-wrapper::after {
		background: linear-gradient(105deg, transparent 35%, rgba(255, 255, 255, 0.38) 50%, transparent 65%) no-repeat;
		background-size: 250% 100%;
		background-position: 130% 0;
	}

	.hero-section:not(.intro-played) .showcase-video-wrapper {
		animation:
			intro-open 1.3s var(--intro-ease) 0.15s backwards,
			intro-shadow 0.5s ease 1.45s backwards;
	}

	.hero-section:not(.intro-played) .showcase-video-wrapper::before {
		animation: intro-frost 1.8s var(--defrost-ease) 0.35s backwards;
	}

	.hero-section:not(.intro-played) .showcase-video-wrapper::after {
		animation: intro-sheen 1.1s ease-in-out 1.3s both;
	}

	.hero-section:not(.intro-played) .showcase-video {
		animation: intro-defrost 1.8s var(--defrost-ease) 0.35s backwards;
	}

	.hero-section:not(.intro-played) .video-toggle {
		animation: intro-fade 0.4s ease 2s backwards;
	}

	.hero-section:not(.intro-played) .hero-creed {
		animation: intro-write 0.9s cubic-bezier(0.22, 1, 0.36, 1) 1.7s backwards;
	}

	.hero-section:not(.intro-played) .hero-pill {
		animation: intro-rise 0.7s var(--ease-spring) backwards;
		animation-delay: calc(1.85s + var(--i, 0) * 60ms);
	}

	/* Seen in the last 12 hours (html.intro-seen, set in app.html): straight to the footage */
	:global(html.intro-seen) .hero-section .showcase-video-wrapper,
	:global(html.intro-seen) .hero-section .showcase-video-wrapper::before,
	:global(html.intro-seen) .hero-section .showcase-video-wrapper::after,
	:global(html.intro-seen) .hero-section .showcase-video,
	:global(html.intro-seen) .hero-section .video-toggle,
	:global(html.intro-seen) .hero-section .hero-creed,
	:global(html.intro-seen) .hero-section .hero-pill {
		animation: none !important;
	}

	/* Page opened in a background tab: wait until it's actually on screen */
	:global(html.intro-hold) .hero-section :global(*),
	:global(html.intro-hold) .hero-section :global(*::before),
	:global(html.intro-hold) .hero-section :global(*::after) {
		animation-play-state: paused !important;
	}

	/* The frame opens out of a smaller, rounder pane */
	@keyframes intro-open {
		from {
			opacity: 0;
			clip-path: inset(9% 12% round calc(var(--radius-card) * 2));
		}
		45% {
			opacity: 1;
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

	/* Frosted and slightly zoomed, the footage clears and settles */
	@keyframes intro-defrost {
		from {
			transform: scale(1.12);
			filter: blur(24px) saturate(1.2) brightness(1.12);
		}
	}

	@keyframes intro-frost {
		from {
			opacity: 1;
		}
	}

	@keyframes intro-sheen {
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
		.hero-section .showcase-video-wrapper,
		.hero-section .showcase-video-wrapper::before,
		.hero-section .showcase-video-wrapper::after,
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
