/** Public origin of the production site. Used to build absolute canonical / Open Graph URLs. */
export const SITE_URL = 'https://lot7.cafe';

export const SITE_NAME = 'LOT 7 CAFE';

export const INSTAGRAM_URL = 'https://instagram.com/lot7.cafe';
export const MAPS_URL = 'https://maps.app.goo.gl/HByZgJ5EC8Uqx9Md7';

/** As listed on the cafe's Google Maps place (MAPS_URL). Drives the Visit card and structured data. */
export const ADDRESS = {
	street: '7 Magnolia St, Queborac Drive',
	area: 'Bagumbayan Sur',
	city: 'Naga City',
	postalCode: '4400',
	region: 'Camarines Sur'
} as const;

/** As listed on the cafe's Google Maps place. `tel` is the international form for tel: links. */
export const PHONE = { display: '0977 413 6345', tel: '+639774136345' } as const;

/** The Google Maps pin */
export const GEO = { latitude: 13.6334402, longitude: 123.1846408 } as const;

/** Every prerendered, indexable page (feeds sitemap.xml) */
export const PAGES = ['/', '/privacy', '/terms'] as const;
