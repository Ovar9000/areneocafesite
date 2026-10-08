<script lang="ts">
	import { clickSpring } from '$lib/attachments/click-spring';
	import { INSTAGRAM_URL } from '$lib/site';

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

<section class="hero-section" id="hero">
	<div class="hero-inner container">
		<h1 class="visually-hidden">Lot 7 Cafe — specialty coffee and vinyl listening room in Naga City</h1>

		<!-- Main Visual: Dynamic Showcase Video (4:5 Portrait on mobile, 16:9 Landscape on desktop) -->
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
			<a href="#story" class="hero-pill">
				<span>THE STORY</span>
			</a>
			<a href="#room" class="hero-pill">
				<span>THE ROOM</span>
			</a>
			<a href="#menu" class="hero-pill">
				<span>MENU</span>
			</a>
			<a href="#sound" class="hero-pill">
				<span>SOUND</span>
			</a>
			<a href="#visit" class="hero-pill">
				<span>VISIT US</span>
			</a>
			<a 
				href={INSTAGRAM_URL} 
				target="_blank" 
				rel="noopener noreferrer" 
				class="hero-pill hero-pill-accent"
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
		overflow: hidden;
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
	.showcase-video-wrapper {
		width: min(92vw, 1150px);
		max-height: calc(75dvh - 5.5rem);
		aspect-ratio: 16 / 9;
		position: relative;
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
		.showcase-video-wrapper {
			width: min(88vw, 360px);
			height: min(48dvh, 420px);
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
