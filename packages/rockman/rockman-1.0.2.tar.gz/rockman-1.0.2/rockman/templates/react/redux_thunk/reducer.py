default_reducer_template = """

        case '{method_name_upper}_{model_name_upper}':
            return {...state, {plural_model_name_lower}: action.payload.{plural_model_name_lower}, error: null, message: action.payload.message};
        case '{method_name_upper}_{model_name_upper}_SUCCESS':
            return {...state, error: null, message: action.payload.message};
        case '{method_name_upper}_FAIL_{model_name_upper}':
            return {...state, error: action.payload.error, message: action.payload.message};
// [ANCHOR_1]
"""

upload_reducer_template = """

        case '{method_name_upper}_{model_name_upper}':
            return {...state, {plural_model_name_lower}: action.payload.{plural_model_name_lower}, error: null, message: action.payload.message};
        case '{method_name_upper}_{model_name_upper}_SUCCESS':
            return {...state, error: null, message: action.payload.message};
        case '{method_name_upper}_FAIL_{model_name_upper}':
            return {...state, error: action.payload.error, message: action.payload.message};
// [ANCHOR_1]
"""