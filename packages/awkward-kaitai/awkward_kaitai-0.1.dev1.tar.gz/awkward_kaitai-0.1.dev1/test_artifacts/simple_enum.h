#ifndef SIMPLE_ENUM_H_
#define SIMPLE_ENUM_H_

// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

#include "kaitai/kaitaistruct.h"
#include <stdint.h>
#include <fstream>
#include "awkward/LayoutBuilder.h"
#include "awkward/utils.h"

using UserDefinedMap = std::map<std::size_t, std::string>;
template<class... BUILDERS>
using RecordBuilder = awkward::LayoutBuilder::Record<UserDefinedMap, BUILDERS...>;
template<std::size_t field_name, class BUILDER>
using RecordField = awkward::LayoutBuilder::Field<field_name, BUILDER>;
template<class PRIMITIVE, class BUILDER>
using ListOffsetBuilder = awkward::LayoutBuilder::ListOffset<PRIMITIVE, BUILDER>;
template<class PRIMITIVE>
using NumpyBuilder = awkward::LayoutBuilder::Numpy<PRIMITIVE>;
template<class PRIMITIVE, class BUILDER>
using IndexedOptionBuilder = awkward::LayoutBuilder::IndexedOption<PRIMITIVE, BUILDER>;
template<class... BUILDERS>
using UnionBuilder = awkward::LayoutBuilder::Union<int8_t, uint32_t, BUILDERS...>;

enum Field_simple_enum : std::size_t {simple_enumA__Zn_triggers};
enum Field_v_one_trig_meta : std::size_t {v_one_trig_metaA__Ztrigger_id, v_one_trig_metaA__Ztrigger_type};

using Simple_enumBuilderType =
	RecordBuilder<
		RecordField<Field_simple_enum::simple_enumA__Zn_triggers, RecordBuilder<
			RecordField<Field_v_one_trig_meta::v_one_trig_metaA__Ztrigger_id, NumpyBuilder<uint32_t>>,
			RecordField<Field_v_one_trig_meta::v_one_trig_metaA__Ztrigger_type, NumpyBuilder<uint32_t>>
		>>
	>;


using V_one_trig_metaBuilderType = decltype(std::declval<Simple_enumBuilderType>().content<Field_simple_enum::simple_enumA__Zn_triggers>());

#if KAITAI_STRUCT_VERSION < 9000L
#error "Incompatible Kaitai Struct Awkward API: version 0.9 or later is required"
#endif

class simple_enum_t : public kaitai::kstruct {

public:
    class v_one_trig_meta_t;

    enum trigger_types_t {
        TRIGGER_TYPES_PHYSICS = 1,
        TRIGGER_TYPES_BORR = 2,
        TRIGGER_TYPES_IRR = 3,
        TRIGGER_TYPES_EORR = 4,
        TRIGGER_TYPES_BCR = 5,
        TRIGGER_TYPES_BORTS = 6,
        TRIGGER_TYPES_EORTS = 7
    };

    simple_enum_t(kaitai::kstream* p__io, kaitai::kstruct* p__parent = 0, simple_enum_t* p__root = 0);

private:
    void _read();
    void _clean_up();

public:
    ~simple_enum_t();

    class v_one_trig_meta_t : public kaitai::kstruct {

    public:

        v_one_trig_meta_t(V_one_trig_metaBuilderType builder, kaitai::kstream* p__io, simple_enum_t* p__parent = 0, simple_enum_t* p__root = 0);

    private:
        void _read();
        void _clean_up();

    public:
        ~v_one_trig_meta_t();

    private:
        uint32_t m_trigger_id;
        trigger_types_t m_trigger_type;
        simple_enum_t* m__root;
        simple_enum_t* m__parent;

    public:
        uint32_t trigger_id() const { return m_trigger_id; }
        trigger_types_t trigger_type() const { return m_trigger_type; }
        simple_enum_t* _root() const { return m__root; }
        simple_enum_t* _parent() const { return m__parent; }
        V_one_trig_metaBuilderType v_one_trig_meta_builder;
    };

private:
    v_one_trig_meta_t* m_n_triggers;
    simple_enum_t* m__root;
    kaitai::kstruct* m__parent;

public:
    v_one_trig_meta_t* n_triggers() const { return m_n_triggers; }
    simple_enum_t* _root() const { return m__root; }
    kaitai::kstruct* _parent() const { return m__parent; }
    Simple_enumBuilderType simple_enum_builder;
};

#ifndef USE_SIMPLE_ENUM_
#define USE_SIMPLE_ENUM_

std::map<std::string, Simple_enumBuilderType*> builder_map;
std::vector<std::string>* builder_keys;

Simple_enumBuilderType* load(std::string file_path);

extern "C" {

    struct Result {
        void* builder;
        const char* error_message;
    };

    Result fill(const char* file_path);

    const char* form(void* builder);

    int64_t length(void* builder);

    int64_t num_buffers(void* builder);

    const char* buffer_name(void* builder, int64_t index);

    int64_t buffer_size(void* builder, int64_t index);

    void copy_into(const char* name, void* from_builder, void* to_buffer, int64_t index);

    void deallocate(void* builder);
}

#endif // USE_SIMPLE_ENUM_


#endif  // SIMPLE_ENUM_H_
