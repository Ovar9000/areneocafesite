export interface CafeStatus {
	isOpen: boolean;
	statusText: string;
	nextChangeText: string;
}

/**
 * Computes cafe status locked explicitly to Asia/Manila timezone (UTC+8),
 * as confirmed from the storefront signage:
 * MON - FRI: 10:00 AM - 10:00 PM
 * SAT: 2:00 PM - 10:00 PM
 * SUN: CLOSED
 */
export function getCafeStatus(now: Date = new Date()): CafeStatus {
	// Format into parts in the cafe's confirmed local timezone
	const formatter = new Intl.DateTimeFormat('en-US', {
		timeZone: 'Asia/Manila',
		weekday: 'short',
		hour: 'numeric',
		minute: 'numeric',
		hour12: false
	});

	const parts = formatter.formatToParts(now);
	let weekday = '';
	let hour = 0;
	let minute = 0;

	for (const p of parts) {
		if (p.type === 'weekday') weekday = p.value;
		if (p.type === 'hour') hour = parseInt(p.value, 10);
		if (p.type === 'minute') minute = parseInt(p.value, 10);
	}

	const currentTime = hour + minute / 60;

	// Sunday: Closed
	if (weekday === 'Sun') {
		return {
			isOpen: false,
			statusText: 'CLOSED (SUNDAY)',
			nextChangeText: 'Opens Monday at 10:00 AM'
		};
	}

	// Saturday: 2:00 PM (14.0) to 10:00 PM (22.0)
	if (weekday === 'Sat') {
		if (currentTime >= 14 && currentTime < 22) {
			return {
				isOpen: true,
				statusText: 'DOORS OPEN NOW',
				nextChangeText: 'Open until 10:00 PM'
			};
		} else if (currentTime < 14) {
			return {
				isOpen: false,
				statusText: 'OPENS AT 2:00 PM',
				nextChangeText: 'Doors open at 2:00 PM today'
			};
		} else {
			return {
				isOpen: false,
				statusText: 'CLOSED FOR THE NIGHT',
				nextChangeText: 'Opens Monday at 10:00 AM'
			};
		}
	}

	// Monday - Friday: 10:00 AM (10.0) to 10:00 PM (22.0)
	if (currentTime >= 10 && currentTime < 22) {
		return {
			isOpen: true,
			statusText: 'DOORS OPEN NOW',
			nextChangeText: 'Open until 10:00 PM'
		};
	} else if (currentTime < 10) {
		return {
			isOpen: false,
			statusText: 'OPENS AT 10:00 AM',
			nextChangeText: 'Doors open at 10:00 AM today'
		};
	} else {
		const nextDayText = weekday === 'Fri' ? 'Opens Saturday at 2:00 PM' : 'Opens tomorrow at 10:00 AM';
		return {
			isOpen: false,
			statusText: 'CLOSED FOR THE NIGHT',
			nextChangeText: nextDayText
		};
	}
}
