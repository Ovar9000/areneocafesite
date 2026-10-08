<script lang="ts">
	import Lot7Logo from './Lot7Logo.svelte';
	import { clickSpring } from '$lib/attachments/click-spring';
	import { INSTAGRAM_URL } from '$lib/site';

	function scrollToTop(e: MouseEvent) {
		e.preventDefault();
		const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
	}
</script>

<!-- One footer, one surface: brand, the Instagram door out, navigation and legal
     all live on a single solid card instead of a banner stacked on a footer. -->
<footer class="site-footer">
	<div class="container">
		<div class="footer-card">
			<!-- Brand & Instagram -->
			<div class="footer-top">
				<div class="footer-brand">
					<a href="/" class="brand-link" aria-label="Lot 7 Cafe home">
						<Lot7Logo height="52px" />
					</a>
					<div class="brand-info">
						<p class="brand-desc font-editorial">
							Specialty coffee &amp; resident vinyl listening room.
						</p>
						<span class="brand-location font-mono">NAGA CITY · CAMARINES SUR · PH</span>
					</div>
				</div>

				<div class="footer-follow">
					<a
						href={INSTAGRAM_URL}
						target="_blank"
						rel="noopener noreferrer"
						class="btn-pill btn-pill-primary follow-btn"
						{@attach clickSpring}
						aria-label="Follow Lot 7 on Instagram @lot7.cafe"
					>
						<svg class="ig-svg-icon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
							<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
							<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
							<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
						</svg>
						<span>FOLLOW @LOT7.CAFE</span>
					</a>
				</div>
			</div>

			<!-- Navigation Jumps -->
			<nav class="footer-nav font-sans" aria-label="Footer navigation">
				<a href="/#story" class="footer-nav-link">THE STORY</a>
				<a href="/#room" class="footer-nav-link">THE ROOM</a>
				<a href="/#menu" class="footer-nav-link">MENU</a>
				<a href="/#sound" class="footer-nav-link">SOUND</a>
				<a href="/#visit" class="footer-nav-link">VISIT US</a>
			</nav>

			<!-- Legal & Back to Top -->
			<div class="footer-bottom font-mono">
				<span class="copyright">© {new Date().getFullYear()} LOT 7 CAFE</span>

				<div class="footer-utilities">
					<a href="/privacy" class="footer-utility-link">PRIVACY</a>
					<a href="/terms" class="footer-utility-link">TERMS</a>
					<a href="/#hero" class="back-top-btn" onclick={scrollToTop} aria-label="Back to top of page">
						<span>TOP</span>
						<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
							<polyline points="18 15 12 9 6 15"></polyline>
						</svg>
					</a>
				</div>
			</div>
		</div>
	</div>
</footer>

<style>
	.site-footer {
		padding: 1rem 0 1.25rem;
		color: var(--text-secondary);
	}

	.footer-card {
		background: var(--bg-surface);
		box-shadow: var(--shadow-card);
		border-radius: var(--radius-card);
		padding: clamp(1.5rem, 4vw, 2.5rem);
		display: flex;
		flex-direction: column;
		gap: 1.75rem;
	}

	/* Brand & Instagram */
	.footer-top {
		display: flex;
		flex-direction: column;
		gap: 1.75rem;
	}

	@media (min-width: 800px) {
		.footer-top {
			flex-direction: row;
			justify-content: space-between;
			align-items: center;
		}
	}

	.footer-brand {
		display: flex;
		align-items: center;
		gap: 1.25rem;
	}

	.brand-link {
		display: flex;
		flex-shrink: 0;
		text-decoration: none;
		transition: transform 0.2s var(--ease-out);
	}

	.brand-link:active {
		transform: scale(0.96);
	}

	.brand-info {
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
	}

	.brand-desc {
		font-size: 1.05rem;
		color: var(--text-main);
		line-height: 1.4;
	}

	.brand-location {
		font-size: 0.68rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
	}

	.footer-follow {
		display: flex;
	}

	.follow-btn {
		padding: 0.75rem 1.5rem;
		font-weight: 700;
	}

	/* Navigation: plain labels that pick up a grey capsule on hover, like an iOS toolbar */
	/* Links are pulled out by their own padding so the text lines up with the content edge;
	   the hairline is drawn on the content edge, not the pulled-out box */
	.footer-nav {
		display: flex;
		flex-wrap: wrap;
		gap: 0.25rem;
		margin: 0 -0.75rem;
		padding-top: 1.25rem;
		position: relative;
	}

	.footer-nav::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0.75rem;
		right: 0.75rem;
		border-top: 1px solid var(--border-subtle);
	}

	.footer-nav-link {
		padding: 0.55rem 0.75rem;
		border-radius: var(--radius-pill);
		font-size: 0.8rem;
		font-weight: 600;
		letter-spacing: 0.06em;
		color: var(--text-secondary);
		text-decoration: none;
		transition: background-color 0.15s ease, color 0.15s ease;
	}

	.footer-nav-link:hover {
		background: var(--fill);
		color: var(--tint);
	}

	/* Legal */
	.footer-bottom {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-between;
		gap: 0.75rem 1.5rem;
		font-size: 0.7rem;
		letter-spacing: 0.08em;
		color: var(--text-muted);
	}

	.footer-utilities {
		display: inline-flex;
		align-items: center;
		gap: 1.25rem;
	}

	.footer-utility-link {
		color: var(--text-muted);
		text-decoration: none;
		transition: color 0.15s ease;
	}

	.footer-utility-link:hover {
		color: var(--tint);
	}

	.back-top-btn {
		display: inline-flex;
		align-items: center;
		gap: 0.35rem;
		min-height: 32px;
		padding: 0.35rem 0.85rem;
		border-radius: var(--radius-pill);
		background: var(--fill);
		color: var(--tint);
		font-weight: 700;
		text-decoration: none;
		transition: background-color 0.15s ease, transform 0.2s var(--ease-out);
	}

	.back-top-btn:hover {
		background: var(--fill-strong);
	}

	.back-top-btn:active {
		transform: scale(0.95);
	}

	/* Phones: a centred stack, like an iOS sheet: brand, one full-width action,
	   an even grid of links, and a single legal line */
	@media (max-width: 799px) {
		.footer-card {
			gap: 1.5rem;
			padding: 2rem 1.25rem 1.5rem;
		}

		.footer-brand {
			flex-direction: column;
			gap: 0.85rem;
			text-align: center;
		}

		.brand-info {
			align-items: center;
		}

		.footer-follow {
			flex-direction: column;
		}

		.follow-btn {
			width: 100%;
			min-height: 50px;
		}

		.footer-nav {
			display: grid;
			grid-template-columns: repeat(6, 1fr);
			gap: 0.5rem;
			margin: 0;
		}

		.footer-nav::before {
			left: 0;
			right: 0;
		}

		/* 3 + 2 layout: each link spans two of six columns, the last row is centred */
		.footer-nav-link {
			grid-column: span 2;
			display: flex;
			align-items: center;
			justify-content: center;
			min-height: 44px;
			padding: 0.5rem;
			background: var(--fill);
			font-size: 0.74rem;
			text-align: center;
		}

		.footer-nav-link:nth-child(4) {
			grid-column: 2 / span 2;
		}

		.footer-bottom {
			flex-direction: column;
			gap: 0.85rem;
		}
	}
</style>
