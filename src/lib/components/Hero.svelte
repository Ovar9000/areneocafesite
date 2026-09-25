<script lang="ts">
	let heroIgBouncing = $state(false);

	function triggerHeroIg() {
		heroIgBouncing = true;
		setTimeout(() => {
			heroIgBouncing = false;
		}, 480);
	}

	function scrollToSection(e: MouseEvent, id: string) {
		e.preventDefault();
		const el = document.getElementById(id);
		if (el) {
			el.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

<section class="hero-section" id="hero">
	<div class="hero-inner container">
		<!-- Main Visual: Dynamic Showcase Video (4:5 Portrait on mobile, 16:9 Landscape on desktop) -->
		<div class="showcase-video-wrapper photo-frame">
			<video 
				src="/videos/lot7-showcase.mp4" 
				poster="/images/video-poster.jpg"
				autoplay
				loop
				muted
				playsinline
				class="showcase-video"
			>
				<track kind="captions" />
			</video>
		</div>

		<!-- Creed Tagline directly below the video -->
		<div class="hero-caption-block">
			<p class="hero-creed font-editorial">
				“...your neighborhood, just a little better.”
			</p>
		</div>

		<!-- Fat Seed Inspired Bottom In-Page Navigation Pills Dock -->
		<nav class="hero-pills-dock font-mono" aria-label="Hero quick jump">
			<a href="#story" class="hero-pill" onclick={(e) => scrollToSection(e, 'story')}>
				<span>THE STORY</span>
			</a>
			<a href="#room" class="hero-pill" onclick={(e) => scrollToSection(e, 'room')}>
				<span>THE ROOM</span>
			</a>
			<a href="#sound" class="hero-pill" onclick={(e) => scrollToSection(e, 'sound')}>
				<span>SOUND</span>
			</a>
			<a href="#visit" class="hero-pill" onclick={(e) => scrollToSection(e, 'visit')}>
				<span>VISIT US</span>
			</a>
			<a 
				href="https://instagram.com/lot7.cafe" 
				target="_blank" 
				rel="noopener noreferrer" 
				class="hero-pill hero-pill-accent"
				class:bouncing={heroIgBouncing}
				onclick={triggerHeroIg}
				aria-label="Lot 7 on Instagram"
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
		background-color: var(--bg-base);
		padding: 1.5rem 0 2rem;
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
		box-shadow: 0 16px 48px rgba(0, 0, 0, 0.08);
	}

	.showcase-video {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
	}

	.hero-caption-block {
		display: flex;
		flex-direction: column;
		align-items: center;
		max-width: 820px;
	}

	.hero-creed {
		font-size: clamp(1.2rem, 2.5vw, 1.75rem);
		color: var(--text-main);
		line-height: 1.35;
		margin: 0;
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

	.hero-pill {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		padding: 0.5rem 1.15rem;
		border-radius: var(--radius-pill);
		border: 1px solid var(--text-main);
		background: #ffffff;
		color: var(--text-main);
		font-size: 0.72rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		text-decoration: none;
		-webkit-tap-highlight-color: transparent !important;
		-webkit-touch-callout: none;
		user-select: none;
		outline: none;
		box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
		transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), 
		            box-shadow 0.2s ease, 
		            background-color 0.2s ease, 
		            color 0.2s ease, 
		            border-color 0.2s ease;
		white-space: nowrap;
		will-change: transform;
	}

	.hero-pill:hover {
		background: var(--text-main);
		color: #ffffff;
		transform: translateY(-2.5px) scale(1.03);
		box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
	}

	.hero-pill:active {
		transform: translateY(1.5px) scale(0.93);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.08s ease;
	}

	.hero-pill.hero-pill-accent {
		gap: 0.4rem;
		border-color: var(--accent-navy);
		color: var(--accent-navy);
		background: #ffffff;
	}

	.hero-pill.hero-pill-accent :global(.ig-svg-icon) {
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
		flex-shrink: 0;
	}

	.hero-pill.hero-pill-accent:hover {
		background: var(--accent-navy);
		border-color: var(--accent-navy);
		color: #ffffff;
		transform: translateY(-2.5px) scale(1.03);
		box-shadow: 0 6px 18px rgba(20, 33, 61, 0.22);
	}

	.hero-pill.hero-pill-accent:hover :global(.ig-svg-icon) {
		transform: rotate(-12deg) scale(1.2);
	}

	.hero-pill.hero-pill-accent:active {
		transform: translateY(2px) scale(0.92);
		box-shadow: 0 2px 4px rgba(20, 33, 61, 0.12);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.08s ease;
	}

	.hero-pill.hero-pill-accent:active :global(.ig-svg-icon) {
		transform: rotate(0deg) scale(0.92);
		transition: transform 0.08s ease;
	}

	.hero-pill.hero-pill-accent.bouncing {
		animation: igClickSpring 0.48s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
	}

	.hero-pill.hero-pill-accent.bouncing :global(.ig-svg-icon) {
		animation: igIconSpin 0.48s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
	}

	@keyframes igClickSpring {
		0% { transform: scale(1); }
		25% { transform: translateY(2px) scale(0.9); }
		55% { transform: translateY(-4px) scale(1.08); }
		75% { transform: translateY(1px) scale(0.97); }
		100% { transform: translateY(0) scale(1); }
	}

	@keyframes igIconSpin {
		0% { transform: rotate(0deg) scale(1); }
		30% { transform: rotate(-18deg) scale(1.28); }
		60% { transform: rotate(12deg) scale(1.15); }
		80% { transform: rotate(-4deg) scale(1.06); }
		100% { transform: rotate(0deg) scale(1); }
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
			border-radius: 18px;
			box-shadow: 0 14px 40px rgba(0, 0, 0, 0.14);
		}

		.hero-creed {
			font-size: clamp(1.05rem, 4.4vw, 1.35rem);
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
			font-size: 0.64rem;
			letter-spacing: 0.04em;
			text-align: center;
		}
	}
</style>
