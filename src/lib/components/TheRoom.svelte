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
		cursor: pointer;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.feature-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

	.feature-media {
		position: relative;
		aspect-ratio: 16 / 9;
		max-height: 480px;
		overflow: hidden;
		background: #ecece7;
	}

	/* Frosted glass light sweep across the tile */
	.feature-media::before,
	.sub-media::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(
			115deg,
			transparent 35%,
			rgba(255, 255, 255, 0.3) 50%,
			transparent 65%
		);
		transform: translateX(-100%);
		transition: transform 0.75s var(--ease-out);
		pointer-events: none;
		z-index: 3;
	}

	/* Frosted glass overlay pane */
	.feature-media::after,
	.sub-media::after {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(
			135deg,
			rgba(255, 255, 255, 0.32) 0%,
			rgba(255, 255, 255, 0.12) 45%,
			rgba(240, 240, 235, 0.28) 100%
		);
		backdrop-filter: blur(10px) saturate(140%) brightness(1.02);
		-webkit-backdrop-filter: blur(10px) saturate(140%) brightness(1.02);
		border: 1px solid rgba(255, 255, 255, 0.45);
		box-shadow: 
			inset 0 0 24px rgba(255, 255, 255, 0.25),
			inset 0 1px 2px rgba(255, 255, 255, 0.6),
			inset 0 -1px 2px rgba(0, 0, 0, 0.05);
		opacity: 0;
		pointer-events: none;
		z-index: 2;
		transition: opacity 0.45s var(--ease-out);
	}

	.gallery-photo {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
		transition: transform 0.65s var(--ease-out), filter 0.5s var(--ease-out);
		will-change: transform, filter;
	}

	.feature-card:hover .gallery-photo,
	.feature-card:focus-within .gallery-photo,
	.sub-card:hover .gallery-photo,
	.sub-card:focus-within .gallery-photo {
		transform: scale(1.05);
		filter: blur(8px) saturate(1.15) brightness(0.96);
	}

	.feature-card:hover .feature-media::after,
	.feature-card:focus-within .feature-media::after,
	.sub-card:hover .sub-media::after,
	.sub-card:focus-within .sub-media::after {
		opacity: 1;
	}

	.feature-card:hover .feature-media::before,
	.feature-card:focus-within .feature-media::before,
	.sub-card:hover .sub-media::before,
	.sub-card:focus-within .sub-media::before {
		transform: translateX(100%);
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
		-webkit-backdrop-filter: blur(8px);
		padding: 0.45rem 0.75rem;
		border-radius: var(--radius-card-sm);
		border: 1px solid var(--border-subtle);
		z-index: 4;
		transition: transform 0.4s var(--ease-out), background 0.3s ease, box-shadow 0.4s ease, border-color 0.3s ease;
	}

	.feature-card:hover .photo-tag,
	.feature-card:focus-within .photo-tag,
	.sub-card:hover .photo-tag,
	.sub-card:focus-within .photo-tag {
		transform: translateY(-2px);
		background: rgba(255, 255, 255, 0.98);
		border-color: rgba(255, 255, 255, 0.85);
		box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
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
		cursor: pointer;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.sub-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
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
