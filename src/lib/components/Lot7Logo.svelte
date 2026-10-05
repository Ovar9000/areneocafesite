<script lang="ts">
	interface Props {
		height?: string;
		class?: string;
		title?: string;
	}

	let { height = '42px', class: className = '', title = 'Lot 7 Cafe' }: Props = $props();
</script>

<!-- width="128" → 64px (1x) and 128px (2x) variants: the badge is never shown wider than ~62px.
     The 2492px master is only read at build time. -->
<enhanced:img
	src="$lib/assets/images/lot7-badge.png"
	alt={title}
	width="128"
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
		border-radius: 8px;
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.16);
	}
</style>
