<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
</script>

<section class="room-section" id="room">
	<div class="room-inner container">
		<!-- Section Header -->
		<div class="room-header">
			<div class="section-label">
				<span class="section-label-dot"></span>
				<span>02 / THE ROOM</span>
			</div>
			
			<div class="header-row">
				<h2 class="section-headline">ROOM ARTIFACTS &amp; ARCHITECTURE</h2>
			</div>
		</div>

		<!-- Asymmetrical Editorial Gallery Layout -->
		<div class="editorial-gallery">
			<!-- Primary Feature: The Backlit License Plate Wall (Wide Landscape) -->
			<article class="feature-card photo-frame">
				<MediaFrame aspect="16 / 9" maxHeight="480px" title="The License Plate Wall" detail="Stamped highway steel">
					<enhanced:img
						src="$lib/assets/images/plate-wall.jpg"
						alt="The Lot 7 license plate wall: rows of American state plates framed in dark wood"
						sizes="(min-width: 1200px) 1088px, 92vw"
						loading="lazy"
					/>
				</MediaFrame>
			</article>

			<!-- Sub-Grid: 2 Paired Cards with Varied Ratios -->
			<div class="sub-gallery-grid">
				<!-- Card 2: Illuminated Box Sign -->
				<article class="sub-card photo-frame">
					<MediaFrame aspect="16 / 10" focus="70% center" title="The Ceiling Sign" detail="Lit overhead, above the bar">
						<enhanced:img
							src="$lib/assets/images/sign-closeup.jpg"
							alt="Close-up of the illuminated Lot 7 Cafe lightbox sign"
							sizes="(min-width: 1200px) 526px, (min-width: 768px) 45vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
				</article>

				<!-- Card 3: The Espresso Bar -->
				<article class="sub-card photo-frame">
					<!-- Portrait source in a landscape frame: keep the portafilter and the cups in view -->
					<MediaFrame aspect="16 / 10" focus="center 52%" title="The Espresso Bar" detail="Pulled to order, iced or hot">
						<enhanced:img
							src="$lib/assets/images/espresso-bar.jpg"
							alt="A barista locking in a portafilter beside iced drinks in Lot 7 cups"
							sizes="(min-width: 1200px) 526px, (min-width: 768px) 45vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
				</article>
			</div>
		</div>
	</div>
</section>

<style>
	.room-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		position: relative;
		box-sizing: border-box;
	}

	.room-header {
		margin-bottom: 3.5rem;
	}

	.header-row {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	@media (min-width: 768px) {
		.header-row {
			flex-direction: row;
			justify-content: space-between;
			align-items: flex-end;
		}
	}

	/* Editorial Gallery */
	.editorial-gallery {
		display: flex;
		flex-direction: column;
		gap: 2.25rem;
	}

	/* Feature Card (Wide) */
	.feature-card {
		display: flex;
		flex-direction: column;
		background: var(--bg-surface);
	}

	/* Sub-grid */
	.sub-gallery-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
	}

	@media (min-width: 768px) {
		.sub-gallery-grid {
			grid-template-columns: 1fr 1fr;
			gap: 2.25rem;
		}
	}

	.sub-card {
		display: flex;
		flex-direction: column;
		background: var(--bg-surface);
	}

	/* Phones: taller crops so the glass caption covers less of each photo */
	@media (max-width: 767px) {
		.editorial-gallery :global(.media-frame) {
			aspect-ratio: 4 / 3 !important;
		}
	}
</style>
