/*
 * Codepage definitions for libvsbsdl
 *
 * Copyright (C) 2023-2024, Joachim Metz <joachim.metz@gmail.com>
 *
 * Refer to AUTHORS for acknowledgements.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#if !defined( _LIBVSBSDL_CODEPAGE_H )
#define _LIBVSBSDL_CODEPAGE_H

#include <libvsbsdl/types.h>

#if defined( __cplusplus )
extern "C" {
#endif

/* The codepage definitions
 */
enum LIBVSBSDL_CODEPAGES
{
	LIBVSBSDL_CODEPAGE_ASCII			= 20127,

	LIBVSBSDL_CODEPAGE_ISO_8859_1			= 28591,
	LIBVSBSDL_CODEPAGE_ISO_8859_2			= 28592,
	LIBVSBSDL_CODEPAGE_ISO_8859_3			= 28593,
	LIBVSBSDL_CODEPAGE_ISO_8859_4			= 28594,
	LIBVSBSDL_CODEPAGE_ISO_8859_5			= 28595,
	LIBVSBSDL_CODEPAGE_ISO_8859_6			= 28596,
	LIBVSBSDL_CODEPAGE_ISO_8859_7			= 28597,
	LIBVSBSDL_CODEPAGE_ISO_8859_8			= 28598,
	LIBVSBSDL_CODEPAGE_ISO_8859_9			= 28599,
	LIBVSBSDL_CODEPAGE_ISO_8859_10			= 28600,
	LIBVSBSDL_CODEPAGE_ISO_8859_11			= 28601,
	LIBVSBSDL_CODEPAGE_ISO_8859_13			= 28603,
	LIBVSBSDL_CODEPAGE_ISO_8859_14			= 28604,
	LIBVSBSDL_CODEPAGE_ISO_8859_15			= 28605,
	LIBVSBSDL_CODEPAGE_ISO_8859_16			= 28606,

	LIBVSBSDL_CODEPAGE_KOI8_R			= 20866,
	LIBVSBSDL_CODEPAGE_KOI8_U			= 21866,

	LIBVSBSDL_CODEPAGE_WINDOWS_874			= 874,
	LIBVSBSDL_CODEPAGE_WINDOWS_932			= 932,
	LIBVSBSDL_CODEPAGE_WINDOWS_936			= 936,
	LIBVSBSDL_CODEPAGE_WINDOWS_949			= 949,
	LIBVSBSDL_CODEPAGE_WINDOWS_950			= 950,
	LIBVSBSDL_CODEPAGE_WINDOWS_1250			= 1250,
	LIBVSBSDL_CODEPAGE_WINDOWS_1251			= 1251,
	LIBVSBSDL_CODEPAGE_WINDOWS_1252			= 1252,
	LIBVSBSDL_CODEPAGE_WINDOWS_1253			= 1253,
	LIBVSBSDL_CODEPAGE_WINDOWS_1254			= 1254,
	LIBVSBSDL_CODEPAGE_WINDOWS_1255			= 1255,
	LIBVSBSDL_CODEPAGE_WINDOWS_1256			= 1256,
	LIBVSBSDL_CODEPAGE_WINDOWS_1257			= 1257,
	LIBVSBSDL_CODEPAGE_WINDOWS_1258			= 1258
};

#define LIBVSBSDL_CODEPAGE_US_ASCII			LIBVSBSDL_CODEPAGE_ASCII

#define LIBVSBSDL_CODEPAGE_ISO_WESTERN_EUROPEAN		LIBVSBSDL_CODEPAGE_ISO_8859_1
#define LIBVSBSDL_CODEPAGE_ISO_CENTRAL_EUROPEAN		LIBVSBSDL_CODEPAGE_ISO_8859_2
#define LIBVSBSDL_CODEPAGE_ISO_SOUTH_EUROPEAN		LIBVSBSDL_CODEPAGE_ISO_8859_3
#define LIBVSBSDL_CODEPAGE_ISO_NORTH_EUROPEAN		LIBVSBSDL_CODEPAGE_ISO_8859_4
#define LIBVSBSDL_CODEPAGE_ISO_CYRILLIC			LIBVSBSDL_CODEPAGE_ISO_8859_5
#define LIBVSBSDL_CODEPAGE_ISO_ARABIC			LIBVSBSDL_CODEPAGE_ISO_8859_6
#define LIBVSBSDL_CODEPAGE_ISO_GREEK			LIBVSBSDL_CODEPAGE_ISO_8859_7
#define LIBVSBSDL_CODEPAGE_ISO_HEBREW			LIBVSBSDL_CODEPAGE_ISO_8859_8
#define LIBVSBSDL_CODEPAGE_ISO_TURKISH			LIBVSBSDL_CODEPAGE_ISO_8859_9
#define LIBVSBSDL_CODEPAGE_ISO_NORDIC			LIBVSBSDL_CODEPAGE_ISO_8859_10
#define LIBVSBSDL_CODEPAGE_ISO_THAI			LIBVSBSDL_CODEPAGE_ISO_8859_11
#define LIBVSBSDL_CODEPAGE_ISO_BALTIC			LIBVSBSDL_CODEPAGE_ISO_8859_13
#define LIBVSBSDL_CODEPAGE_ISO_CELTIC			LIBVSBSDL_CODEPAGE_ISO_8859_14

#define LIBVSBSDL_CODEPAGE_ISO_LATIN_1			LIBVSBSDL_CODEPAGE_ISO_8859_1
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_2			LIBVSBSDL_CODEPAGE_ISO_8859_2
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_3			LIBVSBSDL_CODEPAGE_ISO_8859_3
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_4			LIBVSBSDL_CODEPAGE_ISO_8859_4
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_5			LIBVSBSDL_CODEPAGE_ISO_8859_9
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_6			LIBVSBSDL_CODEPAGE_ISO_8859_10
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_7			LIBVSBSDL_CODEPAGE_ISO_8859_13
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_8			LIBVSBSDL_CODEPAGE_ISO_8859_14
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_9			LIBVSBSDL_CODEPAGE_ISO_8859_15
#define LIBVSBSDL_CODEPAGE_ISO_LATIN_10			LIBVSBSDL_CODEPAGE_ISO_8859_16

#define LIBVSBSDL_CODEPAGE_KOI8_RUSSIAN			LIBVSBSDL_CODEPAGE_KOI8_R
#define LIBVSBSDL_CODEPAGE_KOI8_UKRAINIAN		LIBVSBSDL_CODEPAGE_KOI8_U

#define LIBVSBSDL_CODEPAGE_WINDOWS_THAI			LIBVSBSDL_CODEPAGE_WINDOWS_874
#define LIBVSBSDL_CODEPAGE_WINDOWS_JAPANESE		LIBVSBSDL_CODEPAGE_WINDOWS_932
#define LIBVSBSDL_CODEPAGE_WINDOWS_CHINESE_SIMPLIFIED	LIBVSBSDL_CODEPAGE_WINDOWS_936
#define LIBVSBSDL_CODEPAGE_WINDOWS_KOREAN		LIBVSBSDL_CODEPAGE_WINDOWS_949
#define LIBVSBSDL_CODEPAGE_WINDOWS_CHINESE_TRADITIONAL	LIBVSBSDL_CODEPAGE_WINDOWS_950
#define LIBVSBSDL_CODEPAGE_WINDOWS_CENTRAL_EUROPEAN	LIBVSBSDL_CODEPAGE_WINDOWS_1250
#define LIBVSBSDL_CODEPAGE_WINDOWS_CYRILLIC		LIBVSBSDL_CODEPAGE_WINDOWS_1251
#define LIBVSBSDL_CODEPAGE_WINDOWS_WESTERN_EUROPEAN	LIBVSBSDL_CODEPAGE_WINDOWS_1252
#define LIBVSBSDL_CODEPAGE_WINDOWS_GREEK		LIBVSBSDL_CODEPAGE_WINDOWS_1253
#define LIBVSBSDL_CODEPAGE_WINDOWS_TURKISH		LIBVSBSDL_CODEPAGE_WINDOWS_1254
#define LIBVSBSDL_CODEPAGE_WINDOWS_HEBREW		LIBVSBSDL_CODEPAGE_WINDOWS_1255
#define LIBVSBSDL_CODEPAGE_WINDOWS_ARABIC		LIBVSBSDL_CODEPAGE_WINDOWS_1256
#define LIBVSBSDL_CODEPAGE_WINDOWS_BALTIC		LIBVSBSDL_CODEPAGE_WINDOWS_1257
#define LIBVSBSDL_CODEPAGE_WINDOWS_VIETNAMESE		LIBVSBSDL_CODEPAGE_WINDOWS_1258

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBVSBSDL_CODEPAGE_H ) */

