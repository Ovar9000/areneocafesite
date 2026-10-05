<script lang="ts">
	import { page } from '$app/state';
</script>

<svelte:head>
	<title>{page.status === 404 ? 'PAGE NOT FOUND' : 'SOMETHING WENT WRONG'} — LOT 7 CAFE</title>
	<meta name="robots" content="noindex" />
</svelte:head>

<div class="error-page container">
	<span class="error-code font-mono">{page.status}</span>
	<h1 class="error-title font-display">
		{page.status === 404 ? 'This room doesn’t exist' : 'Something went wrong'}
	</h1>
	<a href="/" class="btn-pill btn-pill-primary">BACK TO LOT 7</a>
</div>

<style>
	.error-page {
		min-height: 60vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 1.25rem;
		padding-top: 4rem;
		padding-bottom: 4rem;
		text-align: center;
	}

	.error-code {
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.15em;
		color: var(--text-muted);
	}

	.error-title {
		font-size: clamp(2.5rem, 7vw, 4.5rem);
		color: var(--text-main);
	}
</style>
