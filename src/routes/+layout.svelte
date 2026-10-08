<script lang="ts">
	// Self-hosted fonts (no requests to Google; each family ships per-subset files with unicode-range)
	import '@fontsource/bebas-neue';
	import '@fontsource-variable/space-grotesk';
	import '@fontsource-variable/newsreader/opsz-italic.css';
	import '@fontsource-variable/jetbrains-mono';
	import '../app.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import ScrollProgress from '$lib/components/ScrollProgress.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.ico" sizes="32x32" />
	<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
</svelte:head>

<a class="skip-link" href="#main-content">Skip to content</a>

<div class="app-root">
	<Header />

	<main id="main-content" tabindex="-1">
		{@render children()}
	</main>

	<Footer />
	<ScrollProgress />
</div>

<style>
	.app-root {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		position: relative;
		overflow-x: clip;
	}

	main {
		flex: 1;
	}

	/* Programmatic focus target for the skip link; no ring around the whole page */
	main:focus {
		outline: none;
	}

	/* Hidden until focused with the keyboard */
	.skip-link {
		position: fixed;
		top: 0.75rem;
		left: 0.75rem;
		z-index: 3000;
		padding: 0.6rem 1rem;
		border-radius: var(--radius-pill);
		background: var(--tint);
		color: #ffffff;
		font-family: var(--font-mono);
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		text-decoration: none;
		transform: translateY(-200%);
	}

	.skip-link:focus-visible {
		transform: none;
	}
</style>
