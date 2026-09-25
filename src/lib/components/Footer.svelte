<script lang="ts">
	import Lot7Logo from './Lot7Logo.svelte';

	let footerIgBouncing = $state(false);

	function triggerFooterIg() {
		footerIgBouncing = true;
		setTimeout(() => {
			footerIgBouncing = false;
		}, 480);
	}

	function scrollToTop(e: MouseEvent) {
		e.preventDefault();
		window.scrollTo({ top: 0, behavior: 'smooth' });
	}
</script>

<footer class="site-footer">
	<div class="footer-inner container">
		<!-- Left: Refined Vector Brand Logo -->
		<div class="footer-brand">
			<Lot7Logo variant="badge" height="34px" />
		</div>

		<!-- Center: Outbound Instagram Door -->
		<div class="footer-social">
			<a 
				href="https://instagram.com/lot7.cafe" 
				target="_blank" 
				rel="noopener noreferrer" 
				class="footer-ig-link font-mono"
				class:bouncing={footerIgBouncing}
				onclick={triggerFooterIg}
				aria-label="Lot 7 Cafe on Instagram"
			>
				<svg class="ig-svg-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
					<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
					<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
				</svg>
				<span>@lot7.cafe</span>
			</a>
		</div>

		<!-- Right: Copyright, Legal & Back to Top -->
		<div class="footer-right font-mono">
			<a href="/#hero" class="back-top-link" onclick={scrollToTop} aria-label="Back to top of page">
				<span>BACK TO TOP</span>
				<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="18 15 12 9 6 15"></polyline>
				</svg>
			</a>
			<div class="footer-legal">
				<a href="/privacy" class="footer-legal-link">PRIVACY</a>
				<span class="legal-bullet">·</span>
				<a href="/terms" class="footer-legal-link">TERMS</a>
			</div>
			<span class="copyright">© 2026 LOT 7 CAFE. NAGA CITY, CAMARINES SUR.</span>
		</div>
	</div>
</footer>

<style>
	.site-footer {
		padding: 2.5rem 0;
		background-color: var(--bg-base);
		border-top: 1px solid var(--border-subtle);
		color: var(--text-muted);
	}

	.footer-inner {
		display: flex;
		flex-direction: column;
		gap: 1.75rem;
		align-items: center;
		justify-content: center;
		text-align: center;
	}

	@media (min-width: 768px) {
		.footer-inner {
			flex-direction: row;
			justify-content: space-between;
			text-align: left;
		}
	}

	.footer-brand {
		display: flex;
		align-items: center;
		justify-content: center;
		text-decoration: none;
		-webkit-tap-highlight-color: transparent !important;
		-webkit-touch-callout: none;
		user-select: none;
		outline: none;
		cursor: pointer;
		transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
		will-change: transform;
	}

	.footer-brand:hover {
		transform: translateY(-2px) scale(1.04);
	}

	.footer-brand:active {
		transform: translateY(1.5px) scale(0.92);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	.footer-social {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.footer-ig-link {
		display: inline-flex;
		align-items: center;
		gap: 0.48rem;
		padding: 0.42rem 0.95rem;
		border-radius: var(--radius-pill);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		color: var(--text-main);
		text-decoration: none;
		font-size: 0.75rem;
		font-weight: 600;
		-webkit-tap-highlight-color: transparent !important;
		-webkit-touch-callout: none;
		user-select: none;
		outline: none;
		box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
		transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), 
		            box-shadow 0.25s ease, 
		            background-color 0.2s ease, 
		            color 0.2s ease, 
		            border-color 0.2s ease;
		will-change: transform;
	}

	.footer-ig-link :global(.ig-svg-icon) {
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
		flex-shrink: 0;
	}

	.footer-ig-link:hover {
		background: var(--accent-navy);
		border-color: var(--accent-navy);
		color: #ffffff;
		transform: translateY(-2.5px) scale(1.03);
		box-shadow: 0 8px 22px rgba(20, 33, 61, 0.22);
	}

	.footer-ig-link:hover :global(.ig-svg-icon) {
		transform: rotate(-12deg) scale(1.2);
	}

	.footer-ig-link:active {
		transform: translateY(2px) scale(0.92);
		box-shadow: 0 2px 4px rgba(20, 33, 61, 0.12);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.08s ease;
	}

	.footer-ig-link:active :global(.ig-svg-icon) {
		transform: rotate(0deg) scale(0.92);
		transition: transform 0.08s ease;
	}

	.footer-ig-link.bouncing {
		animation: igClickSpring 0.48s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
	}

	.footer-ig-link.bouncing :global(.ig-svg-icon) {
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

	.footer-right {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
		gap: 0.45rem;
		font-size: 0.7rem;
		color: var(--text-dim);
	}

	@media (min-width: 768px) {
		.footer-right {
			align-items: flex-end;
			text-align: right;
		}
	}

	.back-top-link {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 0.35rem;
		padding: 0.2rem 0.4rem;
		color: var(--text-muted);
		text-decoration: none;
		font-size: 0.68rem;
		letter-spacing: 0.08em;
		-webkit-tap-highlight-color: transparent !important;
		user-select: none;
		outline: none;
		transition: color 0.15s ease, transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
	}

	.back-top-link:hover {
		color: var(--text-main);
		transform: translateY(-1.5px);
	}

	.back-top-link:active {
		transform: translateY(1px) scale(0.95);
		transition-duration: 0.06s;
	}

	.footer-legal {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 0.5rem;
		font-size: 0.68rem;
		letter-spacing: 0.08em;
	}

	.footer-legal-link {
		color: var(--text-muted);
		text-decoration: none;
		padding: 0.2rem 0.35rem;
		-webkit-tap-highlight-color: transparent !important;
		user-select: none;
		outline: none;
		transition: color 0.15s ease, transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
	}

	.footer-legal-link:hover {
		color: var(--accent-navy);
		text-decoration: underline;
		text-underline-offset: 3px;
		transform: translateY(-1px);
	}

	.footer-legal-link:active {
		transform: translateY(1px) scale(0.95);
		transition-duration: 0.06s;
	}

	.legal-bullet {
		color: var(--border-mid);
	}

	.copyright {
		letter-spacing: 0.05em;
		text-align: center;
	}

	@media (min-width: 768px) {
		.copyright {
			text-align: right;
		}
	}
</style>
