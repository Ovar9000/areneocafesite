<script lang="ts">
	interface Props {
		height?: string;
		class?: string;
		title?: string;
	}

	let { height = '44px', class: className = '', title = 'Lot 7 Cafe' }: Props = $props();
</script>

<!-- Official blue wordmark (design-assets/LOGOS/STICKER.png, trimmed by scripts/export-assets.py).
     width="200" → 100px (1x) and 200px (2x) variants: the mark is never shown wider than ~100px. -->
<enhanced:img
	src="$lib/assets/brand/wordmark-blue.png"
	alt={title}
	width="200"
	style="height: {height}; width: auto;"
	class="lot7-brand-img {className}"
/>

<style>
	.lot7-brand-img {
		display: block;
		flex-shrink: 0;
		object-fit: contain;
		pointer-events: none;
		user-select: none;
		-webkit-user-drag: none;
	}
</style>
