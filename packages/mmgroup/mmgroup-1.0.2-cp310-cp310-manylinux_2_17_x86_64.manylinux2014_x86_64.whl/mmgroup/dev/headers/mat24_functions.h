// Warning: This file has been generated automatically. Do not change!
#ifndef MAT24_FUNCTIONS_H
#define MAT24_FUNCTIONS_H

#include <stdint.h>

/** @file mat24_functions.h
  File ``mat24_functions.h`` is the header file for ``mat24_functions.c``. 
*/

/// @cond DO_NOT_DOCUMENT 

/**************************************************************
#define MAT24_DLL  // We want a DLL!!

// Generic helper definitions for shared library support
#if defined _WIN32 || defined __CYGWIN__
  #define MAT24_HELPER_DLL_IMPORT __declspec(dllimport)
  #define MAT24_HELPER_DLL_EXPORT __declspec(dllexport)
  #define MAT24_HELPER_DLL_LOCAL
#else
  #if __GNUC__ >= 4
    #define MAT24_HELPER_DLL_IMPORT __attribute__ ((visibility ("default")))
    #define MAT24_HELPER_DLL_EXPORT __attribute__ ((visibility ("default")))
    #define MAT24_HELPER_DLL_LOCAL  __attribute__ ((visibility ("hidden")))
  #else
    #define MAT24_HELPER_DLL_IMPORT
    #define MAT24_HELPER_DLL_EXPORT
    #define MAT24_HELPER_DLL_LOCAL
  #endif
#endif

// Now we use the generic helper definitions above to define MAT24_API 
// and MAT24_LOCAL.
// MAT24_API is used for the public API symbols. It either DLL imports 
// or DLL exports (or does nothing for static build). 
// MAT24_LOCAL is used for non-api symbols.

#ifdef MAT24_DLL // defined if MAT24 is compiled as a DLL
  #ifdef MAT24_DLL_EXPORTS // defined if we are building the MAT24 DLL 
                           // (instead of using it)
    #define MAT24_API MAT24_HELPER_DLL_EXPORT
  #else
    #define MAT24_API MAT24_HELPER_DLL_IMPORT
  #endif // MAT24_DLL_EXPORTS
  #define MAT24_LOCAL MAT24_HELPER_DLL_LOCAL
#else // MAT24_DLL is not defined: this means MAT24 is a static lib.
  #define MAT24_API
  #define MAT24_LOCAL
#endif // MAT24_DLL
****************************************************************/

/// @endcond





/// @cond DO_NOT_DOCUMENT 
//  Definitions for using this header in a a DLL (or a shared library)

// Generic helper definitions for DLL (or shared library) support
#if defined _WIN32 || defined __CYGWIN__
  #define MAT24_DLL_IMPORT __declspec(dllimport)
  #define MAT24_DLL_EXPORT __declspec(dllexport)
#else
  #define MAT24_DLL_IMPORT
  #define MAT24_DLL_EXPORT
#endif

// Now we use the generic helper definitions above to define MAT24_API 
// MAT24_API is used for the public API symbols. It either DLL imports 
// or DLL exports 

#ifdef MAT24_DLL_EXPORTS // defined if we are building the MAT24 DLL 
  #define MAT24_API MAT24_DLL_EXPORT
#else                  // not defined if we are using the MAT24 DLL 
  #define MAT24_API  MAT24_DLL_IMPORT
#endif // MAT24_DLL_EXPORTS

/// @endcond
// %%FROM mat24_functions.c

/// @cond DO_NOT_DOCUMENT 

// %%EXPORT_TABLE  p
MAT24_API
extern const uint8_t MAT24_LSBIT_TABLE[32];

/// @endcond  



/**
 @def MAT24_ORDER 
 @brief Order of Mathieu group ``Mat24``. This is equal to 244823040. 
*/
#define MAT24_ORDER 244823040 // Order of Mathieu group Mat24

/**
 @def mat24_def_lsbit24(v1) 
 @brief Macro version of function ``mat24_lsbit24``.
*/
#define mat24_def_lsbit24(v1) MAT24_LSBIT_TABLE[(0x077cb531UL *  \
        ((v1) & (0-(v1))) >> 26) & 0x1f]


/**
 @def mat24_def_lsbit24_pwr2(v1) 
 @brief Special macro version of function ``mat24_lsbit24``.

 This is faster than ``mat24_def_lsbit24``, but here
 ``v1`` must be  power of two. 
*/
#define mat24_def_lsbit24_pwr2(v1)  MAT24_LSBIT_TABLE[(0x077cb531UL *  \
        (v1) >> 26) & 0x1f]


/**
 @def mat24_def_parity12(v1) 
 @brief Parity of vector ``v1`` of 12 bits length.

 Generate a sequence of statements that replaces ``v1`` by
 the bit parity of ``v1 & 0xfff``. 
*/
#define mat24_def_parity12(v1)   v1 ^= v1 >> 6; \
   v1 ^= v1 >> 3; \
   v1 = (0x96 >> (v1 & 7)) & 1;



/**
  @def mat24_def_octad_to_gcode(o)
  @brief Eqivalent to ``mat24_def_octad_to_gcode(o)``

  ``mat24_def_octad_to_gcode(o)`` returns the  number 
  of the Golay code word corresponding to octad ``o``. 
  Parameter ``o`` is not checked.
*/
#define mat24_def_octad_to_gcode(o) (MAT24_OCT_DEC_TABLE[o])


/**
  @def  mat24_def_gcode_to_octad(v)
  @brief Eqivalent to ``mat24_def_gcode_to_octad(v)``

  ``mat24_def_gcode_to_octad(v)`` returns the  number of the
  octad corresponding to Golay code vector ``v``, with ``v``
  in ``gcode``. It returns garbage if ``v`` is not an octad. 
*/
#define mat24_def_gcode_to_octad(v) \
  ((MAT24_OCT_ENC_TABLE[v & 0x7ff] >> 1) \
    + 3 * ((v & 0x7ff) >> 3) - 11)



/**
  @def  mat24_def_not_nonstrict_octad(v)
  @brief Check if ``v`` (or its complement) is an octad.

  Returns 0 if ``v`` (or its complement) is an 
  octad and 1 otherwise.

  Vector ``v`` must be given in ``gcode`` representation
*/
#define mat24_def_not_nonstrict_octad(v) \
    (((MAT24_OCT_ENC_TABLE[(v) & 0x7ff] + 2) & 0x100) >> 8)


/** 
  @def  mat24_def_gcode_to_vect(v)
  @brief Convert Golay code element number ``v`` to a vector in ``GF(2)^24``

  Macro version of function ``mat24_gcode_to_vect``.
*/
#define mat24_def_gcode_to_vect(v) \
    (MAT24_DEC_TABLE1[((v) << 4) & 0xf0]   \
          ^ MAT24_DEC_TABLE2[((v) >> 4) & 0xff])



/** 
  @def  mat24_def_syndrome_from_table(t)
  @brief Convert entry ``t`` of table ``MAT24_SYNDROME_TABLE`` to syndrome

  An entry ``t`` of the table ``MAT24_SYNDROME_TABLE`` encodes an odd
  cocode syndrome. The macro returns that syndrome as a bit vector.
*/
#define mat24_def_syndrome_from_table(t) \
    ((1UL << ((t) & 31)) ^ (1UL << (((t) >> 5) & 31)) \
        ^ (1UL << (((t) >> 10) & 31)))


/// @cond DO_NOT_DOCUMENT 
//  Do not document C functions in the header file!

#ifdef __cplusplus
extern "C" {
#endif
// %%EXPORT p
MAT24_API
uint32_t mat24_lsbit24(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_bw24(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_bit_list(uint32_t v1, uint8_t *a_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_list(uint32_t v1, uint32_t u_len, uint8_t *a_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_extract_b24(uint32_t v1, uint32_t u_mask);
// %%EXPORT p
MAT24_API
uint32_t mat24_spread_b24(uint32_t v1, uint32_t u_mask);
// %%EXPORT_TABLE  p
MAT24_API
extern const uint32_t MAT24_DEC_TABLE0[256];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint32_t MAT24_DEC_TABLE1[256];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint32_t MAT24_DEC_TABLE2[256];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint32_t MAT24_BASIS[24];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint32_t MAT24_RECIP_BASIS[24+8];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint16_t MAT24_SYNDROME_TABLE[0x800];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint16_t MAT24_OCT_DEC_TABLE[759];
// %%EXPORT_TABLE  p
MAT24_API
extern const uint8_t MAT24_OCT_ENC_TABLE[2048];
// %%EXPORT_TABLE 
MAT24_API
extern const uint16_t MAT24_THETA_TABLE[];
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_vintern(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_vintern_to_vect(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_cocode(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_gcode_to_vect(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_to_vect(uint32_t c1);
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_gcode(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_gcode_to_octad(uint32_t v1, uint32_t u_strict);
// %%EXPORT p
MAT24_API
uint32_t mat24_vect_to_octad(uint32_t v1, uint32_t u_strict);
// %%EXPORT p
MAT24_API
uint32_t mat24_octad_to_gcode(uint32_t u_octad);
// %%EXPORT p
MAT24_API
uint32_t mat24_octad_to_vect(uint32_t u_octad);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_syndrome(uint32_t c1, uint32_t u_tetrad);
// %%EXPORT p
MAT24_API
uint32_t mat24_syndrome(uint32_t v1, uint32_t u_tetrad);
// %%EXPORT p
MAT24_API
uint32_t mat24_gcode_weight(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_gcode_to_bit_list(uint32_t v1, uint8_t *a_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_weight(uint32_t c1);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_to_bit_list(uint32_t c1, uint32_t u_tetrad, uint8_t *a_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_to_sextet(uint32_t c1, uint8_t *a_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_scalar_prod(uint32_t v1, uint32_t c1);
// %%EXPORT p
MAT24_API
uint32_t mat24_suboctad_to_cocode(uint32_t u_sub, uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_to_suboctad(uint32_t c1, uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_suboctad_weight(uint32_t u_sub);
// %%EXPORT p
MAT24_API
uint32_t mat24_suboctad_scalar_prod(uint32_t u_sub1, uint32_t u_sub2);
// %%EXPORT p
MAT24_API
uint32_t mat24_cocode_as_subdodecad(uint32_t c1, uint32_t v1, uint32_t u_single);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_theta(uint32_t v1);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_cocycle(uint32_t v1, uint32_t v2);
// %%EXPORT p
MAT24_API
uint32_t mat24_mul_ploop(uint32_t v1, uint32_t v2);
// %%EXPORT p
MAT24_API
uint32_t mat24_pow_ploop(uint32_t v1, uint32_t u_exp);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_comm(uint32_t v1, uint32_t v2);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_cap(uint32_t v1, uint32_t v2);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_assoc(uint32_t v1, uint32_t v2, uint32_t v3);
// %%EXPORT p
MAT24_API
uint32_t mat24_ploop_solve(uint32_t *p_io, uint32_t u_len);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_complete_heptad(uint8_t *p_io);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_check(uint8_t *p1);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_complete_octad(uint8_t *p_io);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_from_heptads(uint8_t *h1, uint8_t *h2, uint8_t *p_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_from_map(uint8_t *h1, uint8_t *h2, uint32_t n, uint8_t *p_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_m24num_to_perm(uint32_t u_m24, uint8_t *p_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_to_m24num(uint8_t  *p1);
// %%EXPORT p
MAT24_API
void mat24_perm_to_matrix(uint8_t  *p1, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_matrix_to_perm(uint32_t *m1, uint8_t *p_out);
// %%EXPORT p
MAT24_API
void mat24_matrix_from_mod_omega(uint32_t *m1);
// %%EXPORT p
MAT24_API
uint32_t mat24_perm_from_dodecads(uint8_t *d1, uint8_t *d2, uint8_t *p_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_op_vect_perm(uint32_t v1, uint8_t *p1);
// %%EXPORT p
MAT24_API
uint32_t mat24_op_gcode_matrix(uint32_t v1, uint32_t *m1);
// %%EXPORT p
MAT24_API
uint32_t mat24_op_gcode_perm(uint32_t v1, uint8_t *p1);
// %%EXPORT p
MAT24_API
uint32_t mat24_op_cocode_perm(uint32_t c1, uint8_t *p1);
// %%EXPORT p
MAT24_API
void mat24_mul_perm(uint8_t *p1, uint8_t *p2, uint8_t *p_out);
// %%EXPORT p
MAT24_API
void mat24_inv_perm(uint8_t *p1, uint8_t *p_out);
// %%EXPORT p
MAT24_API
void mat24_autpl_set_qform(uint32_t *m_io);
// %%EXPORT p
MAT24_API
void mat24_perm_to_autpl(uint32_t c1, uint8_t *p1, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_cocode_to_autpl(uint32_t c1, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_autpl_to_perm(uint32_t *m1, uint8_t  *p_out);
// %%EXPORT p
MAT24_API
uint32_t mat24_autpl_to_cocode(uint32_t *m1);
// %%EXPORT p
MAT24_API
uint32_t mat24_op_ploop_autpl(uint32_t v1, uint32_t *m1);
// %%EXPORT p
MAT24_API
void mat24_mul_autpl(uint32_t *m1, uint32_t *m2, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_inv_autpl(uint32_t *m1, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_perm_to_iautpl(uint32_t c1, uint8_t *p1, uint8_t *p_out, uint32_t *m_out);
// %%EXPORT p
MAT24_API
void mat24_perm_to_net(uint8_t *p1, uint32_t *a_out);
// %%EXPORT p
MAT24_API
void mat24_op_all_autpl(uint32_t *m1, uint16_t *a_out);
// %%EXPORT p
MAT24_API
void mat24_op_all_cocode(uint32_t c1, uint8_t *a_out);
#ifdef __cplusplus
}
#endif

/// @endcond  
//  End condition: Do not document C functions in the header file!




// %%FROM mat24_random.c
#ifdef __cplusplus
extern "C" {
#endif

/** 
  @enum mat24_rand_flags
  @brief Flags describing subgroups of the Mathieu group \f$M_{24}\f$

  This enumeration contains flags describing some subgroups of the
  Mathieu group \f$M_{24}\f$ fixing certain subsets (or sets of
  subsets) of the set \f$\tilde{\Omega} = \{0,\ldots,23\}\f$ on
  which the group \f$M_{24}\f$ acts. Intersetions of these subgroups
  may be described by combining these flags with the bitwise or
  operator ``|``. For each flag we state the set being fixed.

*/
enum mat24_rand_flags {
  MAT24_RAND_2 = 0x01, ///< fixes \f$\{2, 3\} \f$ 
  MAT24_RAND_o = 0x02, ///< fixes \f$\{0, \ldots,7 \}\f$
  MAT24_RAND_t = 0x04, ///< fixes \f$\{\{8i,\ldots,8i+7\} \mid i < 3 \}\f$
  MAT24_RAND_s = 0x08, ///< fixes \f$\{\{4i,\ldots,4i+3\} \mid i < 6 \}\f$
  MAT24_RAND_l = 0x10, ///< fixes \f$\{\{2i, 2i+1\} \mid  4 \leq i < 12 \}\f$
  MAT24_RAND_3 = 0x20, ///< fixes \f$\{1, 2, 3\} \f$ 
};

/// @cond DO_NOT_DOCUMENT 
// %%EXPORT p
MAT24_API
uint32_t mat24_complete_rand_mode(uint32_t u_mode);
// %%EXPORT p
MAT24_API
int32_t mat24_perm_in_local(uint8_t *p1);
// %%EXPORT p
MAT24_API
int32_t mat24_perm_rand_local(uint32_t u_mode, uint32_t u_rand, uint8_t *p_out);
// %%EXPORT p
MAT24_API
int32_t mat24_m24num_rand_local(uint32_t u_mode, uint32_t u_rand);
// %%EXPORT p
MAT24_API
int32_t mat24_m24num_rand_adjust_xy(uint32_t u_mode, uint32_t v);
/// @endcond  
#ifdef __cplusplus
}
#endif

// %%INCLUDE_HEADERS


#endif  //  ifndef MAT24_FUNCTIONS_H

