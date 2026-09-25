<script lang="ts">
	interface Props {
		variant?: 'badge' | 'standalone';
		color?: 'cream' | 'white' | 'blue';
		height?: string | number;
		class?: string;
		title?: string;
	}

	let {
		variant = 'badge',
		color = 'cream',
		height = '42px',
		class: className = '',
		title = 'Lot 7 Cafe'
	}: Props = $props();

	let formattedHeight = $derived(
		typeof height === 'number' ? `${height}px` : height
	);

	let srcWebp = $derived(
		variant === 'badge'
			? '/images/lot7-brand-badge.webp'
			: `/images/lot7-logo-${color}.webp`
	);

	let srcPng = $derived(
		variant === 'badge'
			? '/images/lot7-brand-badge.png'
			: `/images/lot7-logo-${color}.png`
	);
</script>

<picture class="lot7-brand-picture {className}">
	<source srcset={srcWebp} type="image/webp" />
	<img 
		src={srcPng} 
		alt={title}
		style="height: {formattedHeight}; width: auto;"
		class="lot7-brand-img {variant === 'badge' ? 'badge-style' : ''}"
		width={variant === 'badge' ? 2492 : 2010}
		height={variant === 'badge' ? 1442 : 1128}
		loading="eager"
		decoding="async"
	/>
</picture>

<style>
	.lot7-brand-picture {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		vertical-align: middle;
		flex-shrink: 0;
		-webkit-tap-highlight-color: transparent !important;
		-webkit-touch-callout: none;
		user-select: none;
		-webkit-user-select: none;
	}

	.lot7-brand-img {
		display: block;
		object-fit: contain;
		pointer-events: none;
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease, filter 0.2s ease;
		will-change: transform;
		user-select: none;
		-webkit-user-drag: none;
	}

	.badge-style {
		border-radius: 8px;
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.16);
	}
</style>
