<script lang="ts">
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
				<p class="header-desc font-sans">
					Documented on-site. Mismatched stamped metal, backlit wood paneling, and natural day lighting.
				</p>
			</div>
		</div>

		<!-- Asymmetrical Editorial Gallery Layout -->
		<div class="editorial-gallery">
			<!-- Primary Feature: The Backlit License Plate Wall (Wide Landscape) -->
			<article class="feature-card photo-frame">
				<div class="feature-media">
					<img 
						src="/images/brand-plate-wall.png" 
						alt="Lot 7 Signature Backlit License Plate Wall" 
						class="gallery-photo"
					/>
					<div class="photo-tag font-mono">
						<span>SIGNATURE FEATURE WALL</span>
						<span>STAMPED HIGHWAY STEEL</span>
					</div>
				</div>

				<div class="feature-info">
					<div class="feature-headline-group">
						<span class="info-tag font-mono">PRIMARY ARTIFACT</span>
						<h3 class="feature-title font-sans">THE LICENSE PLATE WALL</h3>
					</div>
					<p class="feature-desc font-sans">
						A full wall of authentic mismatched metal license plates from states across the US, set into custom backlit vertical wood paneling.
					</p>
				</div>
			</article>

			<!-- Sub-Grid: 2 Paired Cards with Varied Ratios -->
			<div class="sub-gallery-grid">
				<!-- Card 2: Illuminated Box Sign -->
				<article class="sub-card photo-frame">
					<div class="sub-media sign-media">
						<img 
							src="/images/brand-sign-illuminated.png" 
							alt="Illuminated Lot 7 Box Sign on Ceiling" 
							class="gallery-photo"
						/>
						<div class="photo-tag font-mono">
							<span>CEILING SIGN</span>
							<span>MIRRORED GLASS</span>
						</div>
					</div>
					<div class="sub-info">
						<h4 class="sub-title font-sans">ILLUMINATED CEILING SIGN</h4>
						<p class="sub-desc font-editorial">
							“...your neighborhood, just a little better.”
						</p>
						<span class="sub-meta font-mono">Reflected beneath overhead blue lit box</span>
					</div>
				</article>

				<!-- Card 3: Natural Light Lounge -->
				<article class="sub-card photo-frame">
					<div class="sub-media lounge-media">
						<img 
							src="/images/brand-cafe-lounge.jpg" 
							alt="Interior seating and lounge at Lot 7 Cafe" 
							class="gallery-photo"
						/>
						<div class="photo-tag font-mono">
							<span>MAIN SEATING</span>
							<span>DAYLIGHT</span>
						</div>
					</div>
					<div class="sub-info">
						<h4 class="sub-title font-sans">NATURAL LIGHT LOUNGE</h4>
						<p class="sub-desc font-sans">
							Clean white walls, vintage furnishings, and generous day lighting for conversation and listening.
						</p>
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

	.header-desc {
		color: var(--text-secondary);
		font-size: 0.95rem;
		max-width: 440px;
		line-height: 1.5;
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

	.feature-media {
		position: relative;
		aspect-ratio: 16 / 9;
		max-height: 480px;
		overflow: hidden;
		background: #ecece7;
	}

	.gallery-photo {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
		transition: transform 0.6s var(--ease-out);
	}

	.feature-card:hover .gallery-photo,
	.sub-card:hover .gallery-photo {
		transform: scale(1.03);
	}

	.photo-tag {
		position: absolute;
		bottom: 1rem;
		left: 1rem;
		right: 1rem;
		display: flex;
		justify-content: space-between;
		font-size: 0.65rem;
		letter-spacing: 0.1em;
		color: var(--text-main);
		background: rgba(255, 255, 255, 0.94);
		backdrop-filter: blur(8px);
		padding: 0.45rem 0.75rem;
		border-radius: var(--radius-card-sm);
		border: 1px solid var(--border-subtle);
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
		font-size: 0.65rem;
		letter-spacing: 0.15em;
		color: var(--accent-amber);
		display: block;
		margin-bottom: 0.2rem;
	}

	.feature-title {
		font-size: 1.35rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.feature-desc {
		font-size: 0.9rem;
		color: var(--text-secondary);
		max-width: 500px;
		line-height: 1.5;
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

	.sub-media {
		position: relative;
		overflow: hidden;
		background: #ecece7;
	}

	.sign-media {
		aspect-ratio: 16 / 10;
	}

	.lounge-media {
		aspect-ratio: 16 / 10;
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
		font-size: 0.65rem;
		letter-spacing: 0.08em;
		color: var(--text-dim);
		margin-top: 0.25rem;
	}
</style>
