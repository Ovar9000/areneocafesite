<script lang="ts">
	import { getCafeStatus, type CafeStatus } from '$lib/hours';
	import { INSTAGRAM_URL, MAPS_URL } from '$lib/site';

	// Computed in the browser only: the page is prerendered, so a value computed
	// during the build would be frozen into the HTML that crawlers and previews see.
	let status = $state<CafeStatus | null>(null);

	$effect(() => {
		status = getCafeStatus();
		const interval = setInterval(() => {
			status = getCafeStatus();
		}, 60000);
		return () => clearInterval(interval);
	});
</script>

<section class="visit-section paper-texture" id="visit">
	<div class="visit-inner container">
		<!-- Section Header -->
		<div class="visit-header">
			<div class="section-label">
				<span class="section-label-dot"></span>
				<span>04 / VISIT US</span>
			</div>
			
			<h2 class="section-headline">FIND THE ROOM</h2>
			<p class="visit-subtext font-sans">
				No reservations. Walk in, grab a seat, and push the door open.
			</p>
		</div>

		<!-- 2-Card Intentional Layout: Storefront Hours & Confirmed Location -->
		<div class="visit-grid">
			<!-- Card 1: Authoritative Storefront Hours & Live Local Status -->
			<div class="visit-card photo-frame">
				<div class="card-head font-mono">
					<span class="head-tag">STOREFRONT SIGNAGE HOURS</span>
					<div class="live-pill" class:is-open={status?.isOpen}>
						<span class="live-dot"></span>
						<span>{status?.statusText ?? 'CHECKING HOURS'}</span>
					</div>
				</div>

				<div class="hours-schedule">
					<div class="schedule-row">
						<div class="day-group">
							<span class="day-name font-sans">MON — FRI</span>
							<span class="day-badge font-mono">WEEKDAY</span>
						</div>
						<span class="time-slot font-mono">10:00 AM — 10:00 PM</span>
					</div>

					<div class="schedule-row">
						<div class="day-group">
							<span class="day-name font-sans">SATURDAY</span>
							<span class="day-badge font-mono">WEEKEND</span>
						</div>
						<span class="time-slot font-mono">2:00 PM — 10:00 PM</span>
					</div>

					<div class="schedule-row is-closed">
						<div class="day-group">
							<span class="day-name font-sans">SUNDAY</span>
							<span class="day-badge closed-badge font-mono">CLOSED</span>
						</div>
						<span class="time-slot closed-text font-mono">CLOSED</span>
					</div>
				</div>

				<div class="card-foot font-mono">
					<span class="foot-label">LOCAL STATUS:</span>
					<span class="foot-time">{status?.nextChangeText ?? 'All times in Philippine time'} (Asia/Manila)</span>
				</div>
			</div>

			<!-- Card 2: Confirmed Location & Map Door Out -->
			<div class="visit-card photo-frame">
				<div class="card-head font-mono">
					<span class="head-tag">LOCATION &amp; DIRECTIONS</span>
					<span class="head-city">CAMARINES SUR</span>
				</div>

				<div class="location-body">
					<div class="location-info">
						<span class="location-label font-mono">CONFIRMED LOCATION</span>
						<h3 class="location-city font-sans">NAGA CITY, PHILIPPINES</h3>
						<p class="location-desc font-sans">
							Located in Naga City, Camarines Sur. Tap below for the direct verified GPS pin and real-time driving or walking directions on Google Maps.
						</p>
					</div>

					<!-- Primary Door Out #1: Google Maps Navigation -->
					<div class="location-action">
						<a 
							href={MAPS_URL} 
							target="_blank" 
							rel="noopener noreferrer" 
							class="btn-pill btn-pill-primary map-btn"
						>
							<span>GET DIRECTIONS (GOOGLE MAPS)</span>
							<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
								<polyline points="15 3 21 3 21 9"></polyline>
								<line x1="10" y1="14" x2="21" y2="3"></line>
							</svg>
						</a>
					</div>
				</div>
			</div>
		</div>

		<!-- Primary Door Out #2: The Big Instagram Banner -->
		<div class="instagram-banner photo-frame">
			<div class="ig-inner">
				<div class="ig-copy">
					<div class="section-label ig-label font-mono">
						<span>THE SECOND DOOR OUT</span>
					</div>
					<h3 class="ig-title font-display">FOLLOW @LOT7.CAFE</h3>
				</div>

				<div class="ig-action">
					<a 
						href={INSTAGRAM_URL} 
						target="_blank" 
						rel="noopener noreferrer" 
						class="btn-pill ig-btn"
					>
						<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
							<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
							<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
							<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
						</svg>
						<span>@LOT7.CAFE ON INSTAGRAM</span>
					</a>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.visit-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		background-color: var(--bg-surface);
		border-top: 1px solid var(--border-subtle);
		position: relative;
		box-sizing: border-box;
	}

	.visit-header {
		margin-bottom: 3.5rem;
		text-align: center;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.visit-subtext {
		color: var(--text-secondary);
		font-size: 0.95rem;
		margin-top: 0.5rem;
	}

	/* Grid */
	.visit-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
		margin-bottom: 2.75rem;
	}

	@media (min-width: 800px) {
		.visit-grid {
			grid-template-columns: repeat(2, 1fr);
			gap: 2.5rem;
		}
	}

	.visit-card {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		background: var(--bg-surface);
	}

	.card-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1.15rem 1.5rem;
		border-bottom: 1px solid var(--border-subtle);
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		background: var(--bg-subtle);
	}

	.head-tag {
		color: var(--accent-navy);
		font-weight: 700;
	}

	.head-city {
		color: var(--text-muted);
	}

	.live-pill {
		display: inline-flex;
		align-items: center;
		gap: 0.45rem;
		padding: 0.25rem 0.65rem;
		border-radius: var(--radius-pill);
		background: #ffffff;
		border: 1px solid var(--border-subtle);
		color: var(--text-muted);
		font-size: 0.7rem;
		font-weight: 600;
	}

	.live-pill.is-open {
		background: #f0fdf4;
		border-color: #bbf7d0;
		color: #166534;
	}

	.live-dot {
		width: 6px;
		height: 6px;
		border-radius: 50%;
		background: #a1a1aa;
	}

	.live-pill.is-open .live-dot {
		background: #22c55e;
	}

	/* Hours Schedule */
	.hours-schedule {
		padding: 2rem 1.75rem;
		display: flex;
		flex-direction: column;
		gap: 1.15rem;
	}

	.schedule-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0.85rem 1rem;
		border-radius: var(--radius-card-sm);
		background: var(--bg-subtle);
		border: 1px solid var(--border-subtle);
	}

	.day-group {
		display: flex;
		align-items: center;
		gap: 0.65rem;
	}

	.day-name {
		font-size: 0.9rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.day-badge {
		font-size: 0.7rem;
		padding: 0.15rem 0.4rem;
		border-radius: 3px;
		background: var(--border-subtle);
		color: var(--text-secondary);
	}

	.time-slot {
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--text-main);
	}

	.closed-text {
		color: var(--accent-red);
	}

	.card-foot {
		padding: 1rem 1.5rem;
		background: var(--bg-subtle);
		border-top: 1px solid var(--border-subtle);
		font-size: 0.72rem;
		display: flex;
		gap: 0.5rem;
	}

	.foot-label {
		color: var(--text-muted);
	}

	.foot-time {
		color: var(--text-main);
		font-weight: 600;
	}

	/* Location Body */
	.location-body {
		padding: 2.25rem 2rem;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		gap: 2rem;
		flex: 1;
	}

	.location-info {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.location-label {
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		color: var(--accent-amber-text);
		font-weight: 700;
	}

	.location-city {
		font-size: 1.45rem;
		font-weight: 700;
		color: var(--text-main);
		letter-spacing: -0.01em;
	}

	.location-desc {
		font-size: 0.9rem;
		color: var(--text-secondary);
		line-height: 1.55;
		margin-top: 0.25rem;
	}

	.map-btn {
		width: 100%;
		padding: 0.9rem 1.5rem;
		font-size: 0.85rem;
	}

	/* Instagram Banner */
	.instagram-banner {
		background: var(--accent-navy);
		color: #ffffff;
		padding: 3rem var(--page-padding);
	}

	.ig-inner {
		display: flex;
		flex-direction: column;
		gap: 2rem;
		align-items: flex-start;
		justify-content: space-between;
	}

	@media (min-width: 800px) {
		.ig-inner {
			flex-direction: row;
			align-items: center;
		}
	}

	.ig-copy {
		max-width: 580px;
	}

	.ig-label {
		color: #93c5fd;
		margin-bottom: 0.25rem;
	}

	.ig-title {
		font-size: clamp(2.4rem, 4.5vw, 3.8rem);
		color: #ffffff;
		line-height: 0.95;
		margin: 0.25rem 0 0;
	}

	.ig-btn {
		background: #ffffff;
		color: var(--accent-navy);
		border-color: #ffffff;
		padding: 0.85rem 1.75rem;
		font-weight: 700;
	}

	.ig-btn:focus-visible {
		outline-color: #ffffff;
	}

	.ig-btn:hover {
		background: var(--accent-amber);
		border-color: var(--accent-amber);
		color: #141416;
	}
</style>
