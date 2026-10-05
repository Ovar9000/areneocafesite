<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
</script>

<section class="room-section paper-texture" id="room">
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
				<MediaFrame aspect="16 / 9" maxHeight="480px" tags={['SIGNATURE FEATURE WALL', 'STAMPED HIGHWAY STEEL']}>
					<enhanced:img
						src="$lib/assets/images/plate-wall.jpg"
						alt="Lot 7 Signature Backlit License Plate Wall"
						sizes="(min-width: 1200px) 1088px, 92vw"
						loading="lazy"
					/>
				</MediaFrame>

				<div class="feature-info">
					<div class="feature-headline-group">
						<span class="info-tag font-mono">PRIMARY ARTIFACT</span>
						<h3 class="feature-title font-sans">THE LICENSE PLATE WALL</h3>
					</div>
				</div>
			</article>

			<!-- Sub-Grid: 2 Paired Cards with Varied Ratios -->
			<div class="sub-gallery-grid">
				<!-- Card 2: Illuminated Box Sign -->
				<article class="sub-card photo-frame">
					<MediaFrame aspect="16 / 10" tags={['CEILING SIGN', 'MIRRORED GLASS']}>
						<enhanced:img
							src="$lib/assets/images/sign-illuminated.jpg"
							alt="Illuminated Lot 7 Box Sign on Ceiling"
							sizes="(min-width: 1200px) 526px, (min-width: 768px) 45vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
					<div class="sub-info">
						<h3 class="sub-title font-sans">ILLUMINATED CEILING SIGN</h3>
						<p class="sub-desc font-editorial">
							“...your neighborhood, just a little better.”
						</p>
						<span class="sub-meta font-mono">Reflected beneath overhead blue lit box</span>
					</div>
				</article>

				<!-- Card 3: Natural Light Lounge -->
				<article class="sub-card photo-frame">
					<!-- Portrait source in a landscape frame: keep the counter and the vinyl wall in view -->
					<MediaFrame aspect="16 / 10" focus="center 60%" tags={['MAIN SEATING', 'DAYLIGHT']}>
						<enhanced:img
							src="$lib/assets/images/cafe-lounge.jpg"
							alt="Interior seating and lounge at Lot 7 Cafe"
							sizes="(min-width: 1200px) 526px, (min-width: 768px) 45vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
					<div class="sub-info">
						<h3 class="sub-title font-sans">NATURAL LIGHT LOUNGE</h3>
						<span class="sub-meta font-mono">Floor seating &amp; espresso counter</span>
					</div>
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
		background-color: var(--bg-base);
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
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.feature-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

	.feature-info {
		padding: 1.75rem 2rem;
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	@media (min-width: 768px) {
		.feature-info {
			flex-direction: row;
			align-items: center;
			justify-content: space-between;
		}
	}

	.info-tag {
		font-size: 0.7rem;
		letter-spacing: 0.15em;
		color: var(--accent-amber-text);
		display: block;
		margin-bottom: 0.2rem;
	}

	.feature-title {
		font-size: 1.35rem;
		font-weight: 700;
		color: var(--text-main);
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
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.sub-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

	.sub-info {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 0.45rem;
	}

	.sub-title {
		font-size: 1.1rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.sub-desc {
		font-size: 0.9rem;
		color: var(--text-secondary);
		line-height: 1.45;
	}

	.sub-desc.font-editorial {
		font-size: 1.05rem;
		color: var(--accent-navy);
	}

	.sub-meta {
		font-size: 0.7rem;
		letter-spacing: 0.08em;
		color: var(--text-muted);
		margin-top: 0.25rem;
	}
</style>
