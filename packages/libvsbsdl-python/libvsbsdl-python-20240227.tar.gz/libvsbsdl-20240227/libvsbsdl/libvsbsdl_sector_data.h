/*
 * Chunk data functions
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

#if !defined( _LIBVSBSDL_SECTOR_DATA_H )
#define _LIBVSBSDL_SECTOR_DATA_H

#include <common.h>
#include <types.h>

#include "libvsbsdl_libbfio.h"
#include "libvsbsdl_libcerror.h"
#include "libvsbsdl_libfdata.h"

#if defined( __cplusplus )
extern "C" {
#endif

typedef struct libvsbsdl_sector_data libvsbsdl_sector_data_t;

struct libvsbsdl_sector_data
{
	/* The data
	 */
	uint8_t *data;

	/* The data size
	 */
	size_t data_size;
};

int libvsbsdl_sector_data_initialize(
     libvsbsdl_sector_data_t **sector_data,
     size_t data_size,
     libcerror_error_t **error );

int libvsbsdl_sector_data_free(
     libvsbsdl_sector_data_t **sector_data,
     libcerror_error_t **error );

int libvsbsdl_sector_data_read_file_io_handle(
     libvsbsdl_sector_data_t *sector_data,
     libbfio_handle_t *file_io_handle,
     off64_t sector_offset,
     libcerror_error_t **error );

int libvsbsdl_partition_read_element_data(
     intptr_t *data_handle,
     libbfio_handle_t *file_io_handle,
     libfdata_vector_t *vector,
     libfdata_cache_t *cache,
     int element_index,
     int element_data_file_index,
     off64_t element_data_offset,
     size64_t element_data_size,
     uint32_t element_data_flags,
     uint8_t read_flags,
     libcerror_error_t **error );

#if defined( __cplusplus )
}
#endif

#endif /* !defined( _LIBVSBSDL_SECTOR_DATA_H ) */

