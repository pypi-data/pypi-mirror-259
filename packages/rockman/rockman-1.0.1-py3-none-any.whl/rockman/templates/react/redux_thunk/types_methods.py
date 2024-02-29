default_type_template_anchor_1 = """
export const {method_name_upper} = '{method_name_upper}';
export const {method_name_upper}_SUCCESS = '{method_name_upper}_SUCCESS';
export const {method_name_upper}_FAIL = '{method_name_upper}_FAIL';
// [ANCHOR_1]
"""

default_type_template_anchor_2 = """
// [ANCHOR_2]
interface {model_name_capitalize}{method_name_capitalize}Action {
type: typeof {method_name_upper};
payload: {model_name_capitalize}Response;
}
interface {model_name_capitalize}{method_name_capitalize}SuccessAction {
type: typeof {method_name_upper}_SUCCESS;
payload: {model_name_capitalize}Response;
}
interface {model_name_capitalize}{method_name_capitalize}ErrorAction {
type: typeof {method_name_upper}_FAIL;
payload: {model_name_capitalize}Error;
}
"""

default_type_template_anchor_3 = """
| {model_name_capitalize}{method_name_capitalize}Action 
| {model_name_capitalize}{method_name_capitalize}SuccessAction 
| {model_name_capitalize}{method_name_capitalize}ErrorAction 
// [ANCHOR_3]
"""