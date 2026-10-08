export interface CafeStatus {
	isOpen: boolean;
	statusText: string;
	nextChangeText: string;
}

/** Opening and closing time, in minutes after midnight (Asia/Manila) */
export interface DayHours {
	open: number;
	close: number;
}

export const CAFE_TIMEZONE = 'Asia/Manila';

const daily: DayHours = { open: 10 * 60, close: 22 * 60 };

/**
 * Single source of truth for opening hours, as printed on the official window decal
 * (design-assets/LOGOS/STICKER SLIDING.png):
 * MON - SAT: 10:00 AM - 10:00 PM
 * SUN: CLOSED
 *
 * Indexed like Date#getDay(): 0 = Sunday … 6 = Saturday; null = closed.
 */
export const WEEKLY_HOURS: readonly (DayHours | null)[] = [
	null,
	daily,
	daily,
	daily,
	daily,
	daily,
	daily
];

export const DAY_NAMES = [
	'Sunday',
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday'
] as const;

const SHORT_DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

/** 600 → "10:00 AM", 1320 → "10:00 PM" */
export function formatTime(minutes: number): string {
	const h = Math.floor(minutes / 60);
	const m = minutes % 60;
	const suffix = h < 12 ? 'AM' : 'PM';
	const h12 = h % 12 === 0 ? 12 : h % 12;
	return `${h12}:${String(m).padStart(2, '0')} ${suffix}`;
}

/** 600 → "10:00" (24-hour, for schema.org) */
export function formatTime24(minutes: number): string {
	return `${String(Math.floor(minutes / 60)).padStart(2, '0')}:${String(minutes % 60).padStart(2, '0')}`;
}

/** Day index (0 = Sunday) and minutes after midnight, in the cafe's timezone */
function cafeClock(now: Date): { day: number; minutes: number } {
	const parts = new Intl.DateTimeFormat('en-US', {
		timeZone: CAFE_TIMEZONE,
		weekday: 'short',
		hour: 'numeric',
		minute: 'numeric',
		// h23 guarantees 0–23; `hour12: false` can yield "24" at midnight in some engines
		hourCycle: 'h23'
	}).formatToParts(now);

	const get = (type: string) => parts.find((p) => p.type === type)?.value ?? '';
	const dayIndex = SHORT_DAYS.indexOf(get('weekday'));
	return {
		day: dayIndex >= 0 ? dayIndex : 0,
		minutes: parseInt(get('hour'), 10) * 60 + parseInt(get('minute'), 10)
	};
}

/** Computes the live open/closed status in the cafe's timezone, whatever the visitor's timezone. */
export function getCafeStatus(now: Date = new Date()): CafeStatus {
	const { day, minutes } = cafeClock(now);
	const today = WEEKLY_HOURS[day];

	if (today && minutes >= today.open && minutes < today.close) {
		return {
			isOpen: true,
			statusText: 'DOORS OPEN NOW',
			nextChangeText: `Open until ${formatTime(today.close)}`
		};
	}

	if (today && minutes < today.open) {
		return {
			isOpen: false,
			statusText: `OPENS AT ${formatTime(today.open)}`,
			nextChangeText: `Doors open at ${formatTime(today.open)} today`
		};
	}

	// Closed for the rest of today: find the next day with hours
	for (let offset = 1; offset <= 7; offset++) {
		const nextDay = (day + offset) % 7;
		const next = WEEKLY_HOURS[nextDay];
		if (!next) continue;

		const when = offset === 1 ? 'tomorrow' : DAY_NAMES[nextDay];
		return {
			isOpen: false,
			statusText: today ? 'CLOSED FOR THE NIGHT' : `CLOSED (${DAY_NAMES[day].toUpperCase()})`,
			nextChangeText: `Opens ${when} at ${formatTime(next.open)}`
		};
	}

	return { isOpen: false, statusText: 'CLOSED', nextChangeText: 'Check Instagram for updates' };
}
