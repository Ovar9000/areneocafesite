<script lang="ts">
	import Lot7Logo from './Lot7Logo.svelte';
	import { INSTAGRAM_URL } from '$lib/site';

	function scrollToTop(e: MouseEvent) {
		e.preventDefault();
		const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
	}
</script>

<footer class="site-footer">
	<div class="footer-container container">
		<!-- Top Tier: Brand Identity & In-Page Navigation -->
		<div class="footer-main">
			<!-- Brand Lockup -->
			<div class="footer-brand-lockup">
				<a href="/" class="brand-link" aria-label="Lot 7 Cafe home">
					<Lot7Logo height="42px" />
				</a>
				<div class="brand-info">
					<span class="brand-name font-sans">LOT 7 CAFE</span>
					<p class="brand-desc font-editorial">
						Specialty coffee &amp; resident vinyl listening room.
					</p>
					<span class="brand-location font-mono">Naga City, Camarines Sur, Philippines</span>
				</div>
			</div>

			<!-- Navigation Jumps -->
			<nav class="footer-nav font-sans" aria-label="Footer navigation">
				<a href="/#story" class="footer-nav-link">THE STORY</a>
				<a href="/#room" class="footer-nav-link">THE ROOM</a>
				<a href="/#sound" class="footer-nav-link">SOUND</a>
				<a href="/#visit" class="footer-nav-link">VISIT US</a>
				<a
					href={INSTAGRAM_URL}
					target="_blank"
					rel="noopener noreferrer"
					class="footer-nav-link footer-nav-ext"
					aria-label="Follow Lot 7 on Instagram"
				>
					<span>INSTAGRAM</span>
					<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
						<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
						<polyline points="15 3 21 3 21 9"></polyline>
						<line x1="10" y1="14" x2="21" y2="3"></line>
					</svg>
				</a>
			</nav>
		</div>

		<!-- Bottom Tier: Metadata, Legal & Back to Top on a Unified Baseline -->
		<div class="footer-bottom font-mono">
			<span class="copyright">
				© {new Date().getFullYear()} LOT 7 CAFE. ALL RIGHTS RESERVED.
			</span>

			<div class="footer-utilities">
				<a href="/privacy" class="footer-utility-link">PRIVACY</a>
				<span class="utility-divider" aria-hidden="true">·</span>
				<a href="/terms" class="footer-utility-link">TERMS</a>
				<span class="utility-divider" aria-hidden="true">·</span>
				<a href="/#hero" class="back-top-btn" onclick={scrollToTop} aria-label="Back to top of page">
					<span>BACK TO TOP</span>
					<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
						<polyline points="18 15 12 9 6 15"></polyline>
					</svg>
				</a>
			</div>
		</div>
	</div>
</footer>

<style>
	.site-footer {
		background-color: var(--bg-base);
		border-top: 1px solid var(--border-subtle);
		padding: 4.5rem 0 2.5rem;
		color: var(--text-secondary);
	}

	.footer-container {
		display: flex;
		flex-direction: column;
		gap: 3.25rem;
	}

	/* Top Tier */
	.footer-main {
		display: flex;
		flex-direction: column;
		gap: 2.25rem;
		justify-content: space-between;
		align-items: flex-start;
	}

	@media (min-width: 800px) {
		.footer-main {
			flex-direction: row;
			align-items: flex-start;
		}
	}

	/* Brand Lockup */
	.footer-brand-lockup {
		display: flex;
		align-items: flex-start;
		gap: 1.25rem;
		max-width: 440px;
	}

	.brand-link {
		display: flex;
		align-items: center;
		text-decoration: none;
		flex-shrink: 0;
		transition: transform 0.3s var(--ease-spring);
	}

	.brand-link:hover {
		transform: translateY(-2px) scale(1.04);
	}

	.brand-link:active {
		transform: translateY(1px) scale(0.95);
	}

	.brand-info {
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
	}

	.brand-name {
		font-size: 1.05rem;
		font-weight: 700;
		letter-spacing: 0.05em;
		color: var(--text-main);
	}

	.brand-desc {
		font-size: 0.95rem;
		color: var(--text-secondary);
		line-height: 1.45;
		margin: 0;
	}

	.brand-location {
		font-size: 0.72rem;
		color: var(--text-muted);
		letter-spacing: 0.06em;
		margin-top: 0.2rem;
	}

	/* Nav Links */
	.footer-nav {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 0.75rem 1.75rem;
	}

	@media (min-width: 800px) {
		.footer-nav {
			justify-content: flex-end;
		}
	}

	.footer-nav-link {
		font-size: 0.82rem;
		font-weight: 600;
		letter-spacing: 0.06em;
		color: var(--text-secondary);
		text-decoration: none;
		display: inline-flex;
		align-items: center;
		gap: 0.35rem;
		transition: color 0.15s ease, transform 0.2s var(--ease-spring);
	}

	.footer-nav-link:hover {
		color: var(--accent-navy);
		transform: translateY(-1.5px);
		text-decoration: underline;
		text-underline-offset: 4px;
	}

	.footer-nav-link:active {
		transform: translateY(1px);
	}

	.footer-nav-ext {
		color: var(--accent-navy);
		font-weight: 700;
	}

	/* Bottom Tier */
	.footer-bottom {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		align-items: flex-start;
		justify-content: space-between;
		padding-top: 1.75rem;
		border-top: 1px solid var(--border-subtle);
		font-size: 0.72rem;
		color: var(--text-muted);
	}

	@media (min-width: 768px) {
		.footer-bottom {
			flex-direction: row;
			align-items: center;
		}
	}

	.copyright {
		letter-spacing: 0.05em;
	}

	.footer-utilities {
		display: inline-flex;
		align-items: center;
		gap: 0.65rem;
		flex-wrap: wrap;
	}

	.footer-utility-link {
		color: var(--text-muted);
		text-decoration: none;
		letter-spacing: 0.08em;
		transition: color 0.15s ease;
	}

	.footer-utility-link:hover {
		color: var(--accent-navy);
		text-decoration: underline;
		text-underline-offset: 3px;
	}

	.utility-divider {
		color: var(--border-mid);
	}

	.back-top-btn {
		display: inline-flex;
		align-items: center;
		gap: 0.35rem;
		color: var(--text-main);
		text-decoration: none;
		font-weight: 700;
		letter-spacing: 0.08em;
		padding: 0.3rem 0.65rem;
		border-radius: var(--radius-pill);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
		transition: transform 0.2s var(--ease-spring), background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
	}

	.back-top-btn:hover {
		background: var(--accent-navy);
		border-color: var(--accent-navy);
		color: #ffffff;
		transform: translateY(-1.5px);
	}

	.back-top-btn:active {
		transform: translateY(1px);
	}
</style>
