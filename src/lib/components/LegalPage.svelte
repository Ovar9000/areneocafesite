<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		/** Small label above the title */
		tag: string;
		title: string;
		subtitle: string;
		effective: string;
		/** The policy sections (<section class="legal-section">…) */
		children: Snippet;
	}

	let { tag, title, subtitle, effective, children }: Props = $props();
</script>

<div class="legal-page">
	<div class="legal-container container">
		<!-- Breadcrumb / Back Link -->
		<div class="legal-breadcrumb font-mono">
			<a href="/" class="back-home-link">
				<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
					<polyline points="15 18 9 12 15 6"></polyline>
				</svg>
				<span>BACK TO LOT 7</span>
			</a>
			<span class="legal-date">EFFECTIVE: {effective}</span>
		</div>

		<!-- Title Block -->
		<header class="legal-header">
			<span class="legal-tag font-mono">{tag}</span>
			<h1 class="legal-title font-display">{title}</h1>
			<p class="legal-subtitle font-editorial">“{subtitle}”</p>
		</header>

		<article class="legal-content font-sans">
			{@render children()}
		</article>
	</div>
</div>

<style>
	.legal-page {
		background-color: var(--bg-base);
		padding: 2.5rem 0 5rem;
	}

	.legal-container {
		max-width: 820px;
		margin: 0 auto;
	}

	.legal-breadcrumb {
		display: flex;
		align-items: center;
		justify-content: space-between;
		font-size: 0.72rem;
		letter-spacing: 0.08em;
		margin-bottom: 2rem;
		padding-bottom: 1rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.back-home-link {
		display: inline-flex;
		align-items: center;
		gap: 0.4rem;
		color: var(--text-main);
		text-decoration: none;
		font-weight: 700;
		transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.15s ease;
	}

	.back-home-link:hover {
		color: var(--accent-navy);
		transform: translateX(-3px);
	}

	.legal-date {
		color: var(--text-muted);
	}

	.legal-header {
		margin-bottom: 3rem;
	}

	.legal-tag {
		font-size: 0.72rem;
		font-weight: 700;
		color: var(--accent-navy);
		letter-spacing: 0.12em;
		display: block;
		margin-bottom: 0.5rem;
	}

	.legal-title {
		font-size: clamp(2.5rem, 6vw, 4rem);
		color: var(--text-main);
		line-height: 1;
		margin: 0 0 1rem;
		letter-spacing: -0.02em;
	}

	.legal-subtitle {
		font-size: clamp(1.1rem, 2vw, 1.35rem);
		color: var(--text-secondary);
		line-height: 1.45;
		margin: 0;
	}

	.legal-content {
		display: flex;
		flex-direction: column;
		gap: 2.5rem;
		color: var(--text-secondary);
		font-size: 0.98rem;
		line-height: 1.7;
	}

	/* Section content is written by the page, so it is styled through :global() */
	.legal-content :global(.legal-section) {
		display: flex;
		flex-direction: column;
		gap: 0.85rem;
		padding-bottom: 2rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.legal-content :global(.legal-section:last-child) {
		border-bottom: none;
		padding-bottom: 0;
	}

	.legal-content :global(.section-title) {
		font-size: 0.85rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		color: var(--text-main);
		margin: 0;
	}

	.legal-content :global(.legal-section p) {
		margin: 0;
	}

	.legal-content :global(.legal-section ul) {
		margin: 0.5rem 0 0.5rem 1.25rem;
		display: flex;
		flex-direction: column;
		gap: 0.65rem;
	}

	.legal-content :global(.legal-section a) {
		color: var(--accent-navy);
		text-decoration: underline;
		text-underline-offset: 3px;
		font-weight: 600;
	}

	.legal-content :global(.legal-contact-card) {
		margin-top: 0.75rem;
		padding: 1.25rem 1.5rem;
		border-radius: var(--radius-card-sm);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
		font-size: 0.82rem;
	}

	.legal-content :global(.contact-name) {
		font-weight: 700;
		color: var(--text-main);
	}

	.legal-content :global(.contact-addr),
	.legal-content :global(.contact-ig) {
		color: var(--text-secondary);
	}

	@media (max-width: 640px) {
		.legal-page {
			padding: 1.5rem 0 3.5rem;
		}
	}
</style>
