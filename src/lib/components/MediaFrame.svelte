<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		/** CSS aspect-ratio of the photo window, e.g. "16 / 9" */
		aspect: string;
		maxHeight?: string;
		/** CSS object-position: which part of the photo to keep when cropping */
		focus?: string;
		/** Two caption labels on a pill over the bottom of the photo */
		tags?: [string, string];
		/** The photo, usually an <enhanced:img> (it must live in the parent's template) */
		children: Snippet;
	}

	let { aspect, maxHeight, focus = 'center', tags, children }: Props = $props();
</script>

<!-- Photo window used inside .photo-frame cards: hovering the card zooms the photo,
     sweeps a light reflection across it and lifts the caption pill. -->
<div class="media-frame" style:aspect-ratio={aspect} style:max-height={maxHeight} style:--focus={focus}>
	{@render children()}

	{#if tags}
		<div class="media-tag font-mono">
			<span>{tags[0]}</span>
			<span>{tags[1]}</span>
		</div>
	{/if}
</div>

<style>
	.media-frame {
		position: relative;
		overflow: hidden;
		background: #ecece7;
	}

	.media-frame :global(img) {
		display: block;
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: var(--focus);
		transition: transform 0.65s var(--ease-out);
	}

	/* Light sweep across the photo */
	.media-frame::before {
		content: '';
		position: absolute;
		inset: 0;
		z-index: 3;
		background: linear-gradient(
			115deg,
			transparent 35%,
			rgba(255, 255, 255, 0.3) 50%,
			transparent 65%
		);
		transform: translateX(-100%);
		transition: transform 0.75s var(--ease-out);
		pointer-events: none;
	}

	.media-tag {
		position: absolute;
		bottom: 1rem;
		left: 1rem;
		right: 1rem;
		z-index: 4;
		display: flex;
		justify-content: space-between;
		padding: 0.45rem 0.75rem;
		border-radius: var(--radius-card-sm);
		border: 1px solid var(--border-subtle);
		background: rgba(255, 255, 255, 0.94);
		backdrop-filter: blur(8px);
		-webkit-backdrop-filter: blur(8px);
		color: var(--text-main);
		font-size: 0.7rem;
		letter-spacing: 0.1em;
		transition: transform 0.4s var(--ease-out), background 0.3s ease, box-shadow 0.4s ease, border-color 0.3s ease;
	}

	/* Hover state is driven by the surrounding card */
	:global(.photo-frame:hover) .media-frame :global(img) {
		transform: scale(1.05);
	}

	:global(.photo-frame:hover) .media-frame::before {
		transform: translateX(100%);
	}

	:global(.photo-frame:hover) .media-tag {
		transform: translateY(-2px);
		background: rgba(255, 255, 255, 0.98);
		border-color: rgba(255, 255, 255, 0.85);
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
	}
</style>
