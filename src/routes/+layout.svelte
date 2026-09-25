<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/images/brand-logo-profile.png" />
</svelte:head>

<div class="grain-overlay" aria-hidden="true"></div>

<main class="app-root">
	{@render children()}
</main>

<style>
	.app-root {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		background: var(--bg-void);
		position: relative;
		overflow-x: clip;
	}
</style>
