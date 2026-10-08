<script lang="ts">
	import { getCafeStatus, type CafeStatus } from '$lib/hours';
	import { ADDRESS, MAPS_URL, PHONE } from '$lib/site';

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

	let copied = $state(false);
	let copiedTimer: ReturnType<typeof setTimeout>;

	async function copyAddress() {
		const text = `Lot 7 Cafe, ${ADDRESS.street}, ${ADDRESS.area}, ${ADDRESS.postalCode} ${ADDRESS.city}, ${ADDRESS.region}`;
		try {
			await navigator.clipboard.writeText(text);
		} catch {
			return;
		}
		copied = true;
		clearTimeout(copiedTimer);
		copiedTimer = setTimeout(() => (copied = false), 2500);
	}
</script>

<section class="visit-section plates-rest" id="visit">
	<div class="visit-inner container">
		<!-- Section Header -->
		<div class="visit-header">
			
			<h2 class="section-headline">FIND THE ROOM</h2>
			<p class="visit-subtext font-sans">
				No reservations. Walk in, grab a seat, and push the door open.
			</p>
		</div>

		<div class="visit-grid">
			<!-- Card 1: Hours (from the window decal) & live open/closed status -->
			<div class="visit-card photo-frame">
				<div class="card-head font-mono">
					<h3 class="head-tag">OPENING HOURS</h3>
					<div class="live-pill" class:is-open={status?.isOpen}>
						<span class="live-dot"></span>
						<span>{status?.statusText ?? 'CHECKING HOURS'}</span>
					</div>
				</div>

				<div class="hours-schedule">
					<div class="schedule-row">
						<span class="day-name font-sans">MON — FRI</span>
						<span class="time-slot font-mono">10:00 AM — 10:00 PM</span>
					</div>

					<div class="schedule-row">
						<span class="day-name font-sans">SATURDAY</span>
						<span class="time-slot font-mono">2:00 PM — 10:00 PM</span>
					</div>

					<div class="schedule-row">
						<span class="day-name font-sans">SUNDAY</span>
						<span class="time-slot closed-text font-mono">CLOSED</span>
					</div>
				</div>

				<p class="card-foot font-mono">
					{status?.nextChangeText ?? 'All times in Philippine time'}
				</p>
			</div>

			<!-- Card 2: Address & directions -->
			<div class="visit-card photo-frame">
				<div class="card-head font-mono">
					<h3 class="head-tag">ADDRESS</h3>
					<span class="head-city">NAGA CITY</span>
				</div>

				<div class="location-body">
					<address class="location-info">
						<span class="location-street font-sans">{ADDRESS.street}</span>
						<span class="location-area font-sans">
							{ADDRESS.area}, {ADDRESS.postalCode} {ADDRESS.city}, {ADDRESS.region}
						</span>
						<a href="tel:{PHONE.tel}" class="location-phone font-mono">
							<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
								<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"></path>
							</svg>
							<span><span class="visually-hidden">Call </span>{PHONE.display}</span>
						</a>
					</address>

					<div class="location-action">
						<a
							href={MAPS_URL}
							target="_blank"
							rel="noopener noreferrer"
							class="btn-pill btn-pill-primary map-btn"
						>
							<span>GET DIRECTIONS</span>
							<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
								<polyline points="15 3 21 3 21 9"></polyline>
								<line x1="10" y1="14" x2="21" y2="3"></line>
							</svg>
						</a>
						<!-- For handing to a tricycle or Grab driver -->
						<button type="button" class="btn-pill copy-btn" onclick={copyAddress}>
							{copied ? 'ADDRESS COPIED' : 'COPY ADDRESS'}
						</button>
						<span class="visually-hidden" aria-live="polite">{copied ? 'Address copied' : ''}</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	/* Last section: sized to its content so the footer follows straight on */
	.visit-section {
		display: flex;
		align-items: center;
		padding: 5.5rem 0 3rem;
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
		gap: 0.75rem;
		padding: 1.4rem 1.6rem 0;
		font-size: 0.7rem;
		letter-spacing: 0.12em;
	}

	.head-tag {
		font-size: inherit;
		color: var(--tint);
		font-weight: 700;
	}

	.head-city {
		color: var(--text-muted);
	}

	.live-pill {
		display: inline-flex;
		align-items: center;
		gap: 0.45rem;
		padding: 0.3rem 0.7rem;
		border-radius: var(--radius-pill);
		background: var(--fill);
		color: var(--text-muted);
		font-size: 0.7rem;
		font-weight: 600;
		white-space: nowrap;
	}

	.live-pill.is-open {
		background: rgba(52, 199, 89, 0.14);
		color: #1c6b34;
	}

	.live-dot {
		width: 6px;
		height: 6px;
		border-radius: 50%;
		background: #a1a1aa;
	}

	.live-pill.is-open .live-dot {
		background: #34c759;
	}

	/* Hours Schedule */
	/* iOS inset grouped list: one rounded group, rows split by an inset hairline */
	.hours-schedule {
		margin: 1.25rem;
		display: flex;
		flex-direction: column;
		border-radius: var(--radius-card-sm);
		background: var(--bg-subtle);
		overflow: hidden;
	}

	.schedule-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
		flex-wrap: wrap;
		gap: 0.35rem 1rem;
		min-height: 52px;
		padding: 0.8rem 1.1rem;
		position: relative;
	}

	.schedule-row + .schedule-row::before {
		content: '';
		position: absolute;
		top: 0;
		left: 1.1rem;
		right: 0;
		border-top: 1px solid var(--border-subtle);
	}

	.day-name,
	.time-slot {
		white-space: nowrap;
	}

	.day-name {
		font-size: 0.9rem;
		font-weight: 700;
		color: var(--text-main);
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
		padding: 0 1.6rem 1.5rem;
		font-size: 0.78rem;
		color: var(--text-main);
		font-weight: 600;
	}

	/* Location Body */
	.location-body {
		padding: 1.5rem 1.6rem 1.6rem;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		gap: 2rem;
		flex: 1;
	}

	.location-info {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		font-style: normal;
	}

	.location-street {
		font-size: 1.45rem;
		font-weight: 700;
		color: var(--text-main);
		letter-spacing: -0.01em;
		line-height: 1.2;
	}

	.location-area {
		font-size: 0.95rem;
		color: var(--text-secondary);
		line-height: 1.5;
	}

	/* Tap to call: a 44px target, read as part of the address block */
	.location-phone {
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
		align-self: flex-start;
		min-height: 44px;
		margin-top: 0.15rem;
		font-size: 0.9rem;
		font-weight: 700;
		letter-spacing: 0.04em;
		color: var(--tint);
		text-decoration: none;
	}

	.location-phone:hover {
		text-decoration: underline;
		text-underline-offset: 3px;
	}

	.location-action {
		display: flex;
		flex-direction: column;
		gap: 0.6rem;
	}

	.map-btn,
	.copy-btn {
		width: 100%;
		padding: 0.9rem 1.5rem;
		font-size: 0.85rem;
	}
</style>
