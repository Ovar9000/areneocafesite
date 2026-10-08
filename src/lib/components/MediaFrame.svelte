<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		/** CSS aspect-ratio of the photo window, e.g. "16 / 9" */
		aspect: string;
		maxHeight?: string;
		/** CSS object-position: which part of the photo to keep when cropping */
		focus?: string;
		/** The card's one description: a title and an optional short detail, on a glass caption */
		title?: string;
		detail?: string;
		/** The photo, usually an <enhanced:img> (it must live in the parent's template) */
		children: Snippet;
	}

	let { aspect, maxHeight, focus = 'center', title, detail, children }: Props = $props();
</script>

<!-- Photo window used inside .photo-frame cards. The caption is the card's only text, so a
     photo is never described twice. Deliberately static: no hover zoom or sweep. -->
<figure class="media-frame" style:aspect-ratio={aspect} style:max-height={maxHeight} style:--focus={focus}>
	{@render children()}

	{#if title}
		<figcaption class="media-caption">
			<span class="caption-title font-sans">{title}</span>
			{#if detail}
				<span class="caption-detail font-mono">{detail}</span>
			{/if}
		</figcaption>
	{/if}
</figure>

<style>
	.media-frame {
		/* Without an explicit width, max-height + aspect-ratio would shrink the frame's width too */
		width: 100%;
		position: relative;
		overflow: hidden;
		background: #e5e5ea;
	}

	.media-frame :global(img) {
		display: block;
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: var(--focus);
	}

	/* Floating Liquid Glass caption, inset so its corners stay concentric with the card's */
	.media-caption {
		position: absolute;
		bottom: 0.85rem;
		left: 0.85rem;
		right: 0.85rem;
		z-index: 2;
		display: flex;
		flex-wrap: wrap;
		align-items: baseline;
		justify-content: space-between;
		gap: 0.15rem 1rem;
		padding: 0.7rem 1rem;
		border-radius: calc(var(--radius-card) - 0.85rem);
		background: var(--glass-bg);
		-webkit-backdrop-filter: var(--glass-blur);
		backdrop-filter: var(--glass-blur);
		box-shadow: var(--glass-edge), 0 4px 16px rgba(0, 0, 0, 0.1);
	}

	.caption-title {
		font-size: 0.92rem;
		font-weight: 700;
		letter-spacing: -0.01em;
		text-transform: uppercase;
		color: var(--text-main);
	}

	.caption-detail {
		font-size: 0.68rem;
		letter-spacing: 0.06em;
		color: var(--text-secondary);
	}
</style>
