<script lang="ts">
	const sleeves = [
		{
			title: 'MOVE',
			artist: 'Adam Port, Stryv, Malachiii',
			tag: 'COUNTER ROTATION'
		},
		{
			title: 'SAY WHAT',
			artist: 'feat. Chuala',
			tag: 'COUNTER ROTATION'
		}
	];
</script>

<section class="sound-section paper-texture" id="sound">
	<div class="sound-inner container">
		<!-- Section Header -->
		<div class="sound-header">
			<div class="section-label">
				<span class="section-label-dot"></span>
				<span>03 / SOUND &amp; VINYL</span>
			</div>
			
			<div class="header-row">
				<h2 class="section-headline">RESIDENT DECK &amp; SLEEVES</h2>
				<p class="sound-subtext font-sans">
					Grounded in the physical turntable, near-field studio monitors, and active vinyl rotations kept at the front counter.
				</p>
			</div>
		</div>

		<!-- 2-Column Sound Layout -->
		<div class="sound-grid">
			<!-- Column 1: Hardware & Verified Counter Sleeves -->
			<div class="deck-column">
				<div class="turntable-card photo-frame">
					<div class="turntable-media">
						<img 
							src="/images/interior-turntable-setup.png" 
							alt="Resident Turntable Deck &amp; Studio Monitors at Lot 7" 
							class="turntable-img"
						/>
						<div class="media-tag font-mono">
							<span>RESIDENT DECK</span>
							<span>STUDIO MONITORS</span>
						</div>
					</div>

					<div class="turntable-details">
						<h3 class="card-heading font-sans">DIRECT-DRIVE ANALOG DECK</h3>
						<p class="card-desc font-sans">
							Active listening station behind the bar. Uncompressed analog sound spinning throughout the room during daytime coffee and after-hours.
						</p>
					</div>
				</div>

				<!-- Verified Sleeves Photographed On-Site -->
				<div class="sleeves-box photo-frame">
					<div class="sleeves-head font-mono">
						<span>CONFIRMED SLEEVES AT THE BAR</span>
						<span class="status-verified">ON ROTATION</span>
					</div>

					<div class="sleeves-list">
						{#each sleeves as s, i}
							<div class="sleeve-item">
								<span class="sleeve-idx font-mono">0{i + 1}</span>
								<div class="sleeve-info">
									<span class="sleeve-title font-sans">{s.title}</span>
									<span class="sleeve-artist font-sans">{s.artist}</span>
								</div>
								<span class="sleeve-tag font-mono">{s.tag}</span>
							</div>
						{/each}
					</div>
				</div>
			</div>

			<!-- Column 2: Archival Soft-Opening Record (Strictly Dated Past Event) -->
			<div class="archive-column">
				<div class="archive-card photo-frame">
					<div class="archive-top font-mono">
						<span class="archive-pill">PAST EVENTS</span>
						<span class="archive-date font-mono">09.08.26 · 5:00 PM</span>
					</div>

					<div class="archive-poster-wrap">
						<img 
							src="/images/brand-soft-opening-poster.png" 
							alt="Lot 7 Soft Opening Poster: 09.08.26 featuring Vinz, Pancake, Bos, Kim, Suki" 
							class="archive-poster"
						/>
					</div>

					<div class="archive-caption">
						<span class="lineup-label font-mono">SOFT OPENING LINEUP:</span>
						<p class="lineup-names font-display">
							VINZ · PANCAKE · BOS · KIM · SUKI
						</p>

						<div class="archive-subline font-mono">
							<span>POP-UP BY GROOVY</span>
							<span>“YOUR NEIGHBORHOOD, JUST A LITTLE BETTER.”</span>
						</div>

						<p class="archive-note font-sans">
							Archival record of our soft opening. For future unannounced listening sessions and guest selectors, check our Instagram stories.
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.sound-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		background-color: var(--bg-surface);
		border-top: 1px solid var(--border-subtle);
		border-bottom: 1px solid var(--border-subtle);
		position: relative;
		box-sizing: border-box;
	}

	.sound-header {
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

	.sound-subtext {
		color: var(--text-secondary);
		font-size: 0.95rem;
		max-width: 480px;
		line-height: 1.5;
	}

	/* Grid */
	.sound-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2.25rem;
		align-items: flex-start;
	}

	@media (min-width: 900px) {
		.sound-grid {
			grid-template-columns: 1.25fr 1fr;
			gap: 2.75rem;
		}
	}

	.deck-column, .archive-column {
		display: flex;
		flex-direction: column;
		gap: 1.75rem;
	}

	/* Turntable Card */
	.turntable-card {
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
	}

	.turntable-media {
		position: relative;
		aspect-ratio: 4 / 3;
		overflow: hidden;
		background: #ecece7;
	}

	.turntable-img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		display: block;
		transition: transform 0.6s var(--ease-out);
	}

	.turntable-card:hover .turntable-img {
		transform: scale(1.03);
	}

	.media-tag {
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

	.turntable-details {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.card-heading {
		font-size: 1.2rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.card-desc {
		font-size: 0.88rem;
		color: var(--text-muted);
		line-height: 1.5;
	}

	/* Sleeves Box */
	.sleeves-box {
		padding: 1.5rem;
		background: var(--bg-surface);
	}

	.sleeves-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.68rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
		padding-bottom: 0.75rem;
		border-bottom: 1px solid var(--border-subtle);
		margin-bottom: 1rem;
	}

	.status-verified {
		color: var(--accent-green);
		font-weight: 700;
	}

	.sleeves-list {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.sleeve-item {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.75rem 1rem;
		background: var(--bg-subtle);
		border-radius: var(--radius-card-sm);
		border: 1px solid var(--border-subtle);
	}

	.sleeve-idx {
		font-size: 0.75rem;
		font-weight: 700;
		color: var(--accent-navy);
	}

	.sleeve-info {
		flex: 1;
		display: flex;
		flex-direction: column;
	}

	.sleeve-title {
		font-size: 0.95rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.sleeve-artist {
		font-size: 0.78rem;
		color: var(--text-muted);
	}

	.sleeve-tag {
		font-size: 0.62rem;
		color: var(--text-dim);
	}

	/* Archival Card */
	.archive-card {
		padding: 1.75rem;
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
	}

	.archive-top {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.68rem;
		letter-spacing: 0.1em;
		padding-bottom: 0.5rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.archive-pill {
		color: var(--accent-navy);
		font-weight: 700;
	}

	.archive-date {
		color: var(--accent-amber);
		font-weight: 700;
	}

	.archive-poster-wrap {
		width: 100%;
		border-radius: var(--radius-card-sm);
		overflow: hidden;
		background: #14213d;
		padding: 1rem;
		display: flex;
		justify-content: center;
	}

	.archive-poster {
		max-height: 290px;
		width: auto;
		object-fit: contain;
		display: block;
		border-radius: 4px;
	}

	.archive-caption {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.lineup-label {
		font-size: 0.65rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
	}

	.lineup-names {
		font-size: clamp(1.4rem, 2.5vw, 1.85rem);
		letter-spacing: 0.04em;
		color: var(--text-main);
		line-height: 1.05;
	}

	.archive-subline {
		display: flex;
		flex-direction: column;
		gap: 0.2rem;
		font-size: 0.65rem;
		letter-spacing: 0.08em;
		color: var(--text-muted);
		padding: 0.5rem 0;
		border-top: 1px dashed var(--border-subtle);
		border-bottom: 1px dashed var(--border-subtle);
	}

	.archive-note {
		font-size: 0.82rem;
		color: var(--text-secondary);
		line-height: 1.5;
	}
</style>
