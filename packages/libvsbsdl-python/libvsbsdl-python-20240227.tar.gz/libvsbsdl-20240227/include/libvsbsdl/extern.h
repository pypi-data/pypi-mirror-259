/*
 * The extern definition
 *
 * This header should be included in header files that export or import
 * library functions
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

#if !defined( _LIBVSBSDL_EXTERN_H )
#define _LIBVSBSDL_EXTERN_H

/* To export functions from the libvsbsdl DLL define LIBVSBSDL_DLL_EXPORT
 * To import functions from the libvsbsdl DLL define LIBVSBSDL_DLL_IMPORT
 * Otherwise use default extern statement
 */
#if defined( LIBVSBSDL_DLL_EXPORT )
#define LIBVSBSDL_EXTERN __declspec(dllexport)

#elif defined( LIBVSBSDL_DLL_IMPORT )
#define LIBVSBSDL_EXTERN extern __declspec(dllimport)

#else
#define LIBVSBSDL_EXTERN extern

#endif

#endif /* !defined( _LIBVSBSDL_EXTERN_H ) */

