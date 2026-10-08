<script lang="ts">
	import type { Picture } from 'vite-imagetools';
	import MediaFrame from './MediaFrame.svelte';

	// Every gallery photo, run through the same AVIF/WebP + srcset pipeline as <enhanced:img> literals
	const files = import.meta.glob<{ default: Picture }>('/src/lib/assets/images/gallery-*.jpg', {
		eager: true,
		query: { enhanced: true }
	});

	interface Photo {
		file: string;
		title: string;
		detail: string;
		alt: string;
		landscape?: boolean;
		focus?: string;
	}

	// Portraits and landscapes alternate so the strip has a rhythm
	const PHOTOS: Photo[] = [
		{ file: 'pour', title: 'The Pour', detail: 'Milk over espresso', alt: 'Milk being poured into an iced espresso on the drip tray' },
		{ file: 'lightbox', title: 'The Lightbox', detail: 'After dark', alt: 'The Lot 7 Cafe lightbox glowing on the dark ceiling: your neighborhood, just a little better.', landscape: true },
		{ file: 'handoff', title: 'Order Up', detail: 'Iced, to the counter', alt: 'A barista setting two iced lattes in Lot 7 cups on the counter' },
		{ file: 'cups', title: 'House Cups', detail: 'Ready on the bar', alt: 'Empty Lot 7 cups lined up on the bar, the espresso machine behind' },
		{ file: 'rush', title: 'Rush Hour', detail: 'Long exposure', alt: 'A long-exposure blur of people moving through the cafe', landscape: true },
		{ file: 'grinder', title: 'The Grinder', detail: 'Dialled in daily', alt: 'The espresso grinder and machine at the end of the counter', focus: 'center 60%' },
		{ file: 'booth', title: 'The Booth', detail: 'Under the sign', alt: 'A DJ at the booth by the window, the Lot 7 lightbox overhead' },
		{ file: 'iced-black', title: 'Iced Black', detail: 'On the wood', alt: 'An iced black coffee in a Lot 7 cup on a wooden ledge', landscape: true },
		{ file: 'soda', title: 'Green Soda', detail: 'From the B-Sides', alt: 'A hand lifting a green soda in a Lot 7 cup from the counter', focus: 'center 60%' },
		{ file: 'portrait', title: 'In the Moment', detail: 'Night session', alt: 'A guest looking down in warm flash light under the ceiling lettering' },
		{ file: 'ceiling', title: 'Overhead', detail: 'The grid ceiling', alt: 'The black metal grid ceiling of the cafe', landscape: true }
	];

	const picture = (file: string) => files[`/src/lib/assets/images/gallery-${file}.jpg`].default;

	let track: HTMLElement;
	let atStart = $state(true);
	let atEnd = $state(false);

	function update() {
		atStart = track.scrollLeft < 8;
		atEnd = track.scrollLeft + track.clientWidth > track.scrollWidth - 8;
	}

	function page(direction: 1 | -1) {
		const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		track.scrollBy({ left: direction * track.clientWidth * 0.8, behavior: reduceMotion ? 'auto' : 'smooth' });
	}

	$effect(() => {
		update();
		const observer = new ResizeObserver(update);
		observer.observe(track);
		return () => observer.disconnect();
	});
</script>

<section class="gallery-section" id="gallery">
	<div class="gallery-header container">
		<h2 class="section-headline">AROUND THE ROOM</h2>

		<!-- Glass paging buttons; the strip also swipes, scrolls and takes arrow keys -->
		<div class="gallery-controls">
			<button type="button" class="gallery-btn glass" onclick={() => page(-1)} disabled={atStart} aria-label="Previous photos">
				<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
					<polyline points="15 18 9 12 15 6"></polyline>
				</svg>
			</button>
			<button type="button" class="gallery-btn glass" onclick={() => page(1)} disabled={atEnd} aria-label="Next photos">
				<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
					<polyline points="9 18 15 12 9 6"></polyline>
				</svg>
			</button>
		</div>
	</div>

	<!-- A scrollable region must be reachable by keyboard so it can be scrolled with the arrow keys -->
	<div class="container">
		<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
		<div
			class="gallery-track"
			class:more-before={!atStart}
			class:more-after={!atEnd}
			bind:this={track}
			onscroll={update}
			tabindex="0"
			role="region"
			aria-label="Photo gallery, scrolls sideways"
		>
			{#each PHOTOS as photo (photo.file)}
				<div class="gallery-card photo-frame" class:landscape={photo.landscape}>
					<MediaFrame aspect={photo.landscape ? '3 / 2' : '2 / 3'} focus={photo.focus} title={photo.title} detail={photo.detail}>
						<enhanced:img
							src={picture(photo.file)}
							alt={photo.alt}
							sizes={photo.landscape ? '(min-width: 900px) 690px, 510px' : '(min-width: 900px) 310px, 230px'}
							loading="lazy"
						/>
					</MediaFrame>
				</div>
			{/each}
		</div>
	</div>
</section>

<style>
	.gallery-section {
		padding: 5.5rem 0 3rem;
		--card-h: clamp(340px, 55vh, 460px);
	}

	.gallery-header {
		display: flex;
		align-items: flex-end;
		justify-content: space-between;
		gap: 1rem;
		margin-bottom: 2rem;
	}

	.gallery-controls {
		display: flex;
		gap: 0.5rem;
		flex-shrink: 0;
	}

	.gallery-btn {
		display: grid;
		place-items: center;
		width: 44px;
		height: 44px;
		border: none;
		border-radius: 50%;
		color: var(--tint);
		cursor: pointer;
		transition: opacity 0.2s ease, scale 0.2s var(--ease-out);
	}

	.gallery-btn:active:not(:disabled) {
		scale: 0.92;
	}

	.gallery-btn:disabled {
		opacity: 0.4;
		cursor: default;
	}

	/* The strip stays inside the content column like every other section. A few pixels of
	   side padding give the card shadows room without visibly breaking the margin. */
	.gallery-track {
		--fade-before: 0px;
		--fade-after: 0px;
		display: flex;
		gap: 1rem;
		margin-inline: -6px;
		padding: 0.5rem 6px 1.75rem;
		overflow-x: auto;
		overscroll-behavior-x: contain;
		scroll-snap-type: x mandatory;
		scroll-padding-inline: 6px;
		scrollbar-width: none;
		/* A soft fade only on a side that has more photos to scroll to */
		-webkit-mask-image: linear-gradient(90deg, transparent, #000 var(--fade-before), #000 calc(100% - var(--fade-after)), transparent);
		mask-image: linear-gradient(90deg, transparent, #000 var(--fade-before), #000 calc(100% - var(--fade-after)), transparent);
	}

	.gallery-track.more-before {
		--fade-before: 3rem;
	}

	.gallery-track.more-after {
		--fade-after: 3rem;
	}

	.gallery-track::-webkit-scrollbar {
		display: none;
	}

	.gallery-track:focus-visible {
		outline-offset: -2px;
	}

	.gallery-card {
		flex: none;
		height: var(--card-h);
		aspect-ratio: 2 / 3;
		scroll-snap-align: start;
	}

	.gallery-card.landscape {
		aspect-ratio: 3 / 2;
		/* Never wider than the strip: on a phone a 3:2 card would hang off-screen with its
		   caption cut. It keeps the portraits' height and the photo crops to fit. */
		max-width: 100%;
	}

	.gallery-card.landscape :global(.media-frame) {
		aspect-ratio: auto !important;
		height: 100%;
	}

	@media (max-width: 767px) {
		.gallery-section {
			--card-h: 340px;
		}

		.gallery-track {
			gap: 0.75rem;
		}

		/* Narrow cards: a slimmer fade so it never eats a caption */
		.gallery-track.more-before {
			--fade-before: 1rem;
		}

		.gallery-track.more-after {
			--fade-after: 1rem;
		}
	}
</style>
