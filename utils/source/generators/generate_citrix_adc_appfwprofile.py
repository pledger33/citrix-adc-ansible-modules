import os
import copy
import json
import yaml
from jinja2 import Environment, FileSystemLoader

from helpers import calculate_transforms_for_attribute, calculate_doc_list, calculate_attributes_config_dict


HERE = os.path.abspath(os.path.dirname(__file__))

def populate_template(template_dir, **kwargs):
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(template_dir),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template('citrix_adc_appfwprofile.template')
    stream = template.stream(**kwargs)

    #output_file = 'citrix_adc_appfw_profile.py'
    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adc_appfw_profile.py')
    stream.dump(
        output_file,
        encoding='utf-8'
    )


def main():
    with open(os.path.join(HERE, 'generator_options.yaml'), 'r') as fh:
        options = yaml.load(fh)

    # Find template dir
    template_dir = os.path.join(HERE, '..', 'templates', 'appfw')
    if not os.path.exists(template_dir):
        raise Exception('Cannot find template dir')

    # Find nscli json data dir
    json_dir = os.path.join(HERE, options['nitro_api_defines'])
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')

    main_json_file = os.path.join(json_dir, 'appfwprofile.json')
    with open(main_json_file, 'r') as fh:
        main_object_attributes = json.load(fh)

    main_object_doc_list = calculate_doc_list(main_object_attributes, skip_attributes=['newname'])

    attributes_config_list = []
    attributes_config_list.append(
        calculate_attributes_config_dict('appfwprofile', main_object_attributes, skip_attributes=['newname'])
    )

    # Add the bindings objects
    bindings = []

    def append_bindings(json_file, binding_dict):
        with open(json_file, 'r') as fh:
            attributes = json.load(fh)

        key = binding_dict['binding_key']
        binding_dict.update({
            'attributes_config_list': calculate_attributes_config_dict(key, attributes),
        })
        doc_list = copy.deepcopy(binding_dict['attributes_config_list']['attributes'])
        doc_list.remove(binding_dict['link_to_main']['bind_key'])
        binding_dict['doc_list'] = doc_list
        bindings.append(binding_dict)
        attributes_config_list.append(binding_dict['attributes_config_list'])


    # contenttype bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_contenttype_binding.json'),
        binding_dict={
            'binding_key': 'contenttype_bindings',
            'description': 'contenttype bindings',
            'binding_object': 'appfwprofile_contenttype_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # cookieconsistency
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_cookieconsistency_binding.json'),
        binding_dict={
            'binding_key': 'cookieconsistency_bindings',
            'description': 'cookieconsistency bindings',
            'binding_object': 'appfwprofile_cookieconsistency_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # creditcardnumber
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_creditcardnumber_binding.json'),
        binding_dict={
            'binding_key': 'creditcardnumber_bindings',
            'description': 'creditcardnumber bindings',
            'binding_object': 'appfwprofile_creditcardnumber_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # crosssitescripting
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_crosssitescripting_binding.json'),
        binding_dict={
            'binding_key': 'crosssitescripting_bindings',
            'description': 'crosssitescripting bindings',
            'binding_object': 'appfwprofile_crosssitescripting_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # csrftag
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_csrftag_binding.json'),
        binding_dict={
            'binding_key': 'csrftag_bindings',
            'description': 'csrftag bindings',
            'binding_object': 'appfwprofile_csrftag_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # denyurl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_denyurl_binding.json'),
        binding_dict={
            'binding_key': 'denyurl_bindings',
            'description': 'denyurl bindings',
            'binding_object': 'appfwprofile_denyurl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # excluderescontenttype bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_excluderescontenttype_binding.json'),
        binding_dict={
            'binding_key': 'excluderescontenttype_bindings',
            'description': 'excluderescontenttype bindings',
            'binding_object': 'appfwprofile_excluderescontenttype_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # fieldconsistency bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_fieldconsistency_binding.json'),
        binding_dict={
            'binding_key': 'fieldconsistency_bindings',
            'description': 'fieldconsistency bindings',
            'binding_object': 'appfwprofile_fieldconsistency_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # fieldformat bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_fieldformat_binding.json'),
        binding_dict={
            'binding_key': 'fieldformat_bindings',
            'description': 'fieldformat bindings',
            'binding_object': 'appfwprofile_fieldformat_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # FIXME file bug for as_expression -> expression
    # safeobject bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_safeobject_binding.json'),
        binding_dict={
            'binding_key': 'safeobject_bindings',
            'description': 'safeobject bindings',
            'binding_object': 'appfwprofile_safeobject_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # sqlinjection bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_sqlinjection_binding.json'),
        binding_dict={
            'binding_key': 'sqlinjection_bindings',
            'description': 'sqlinjection bindings',
            'binding_object': 'appfwprofile_sqlinjection_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # starturl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_starturl_binding.json'),
        binding_dict={
            'binding_key': 'starturl_bindings',
            'description': 'starturl bindings',
            'binding_object': 'appfwprofile_starturl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # trustedlearningclients bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_trustedlearningclients_binding.json'),
        binding_dict={
            'binding_key': 'trustedlearningclients_bindings',
            'description': 'trustedlearningclients bindings',
            'binding_object': 'appfwprofile_trustedlearningclients_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmlattachmenturl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmlattachmenturl_binding.json'),
        binding_dict={
            'binding_key': 'xmlattachmenturl_bindings',
            'description': 'xmlattachmenturl bindings',
            'binding_object': 'appfwprofile_xmlattachmenturl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmldosurl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmldosurl_binding.json'),
        binding_dict={
            'binding_key': 'xmldosurl_bindings',
            'description': 'xmldosurl bindings',
            'binding_object': 'appfwprofile_xmldosurl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmlsqlinjection bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmlsqlinjection_binding.json'),
        binding_dict={
            'binding_key': 'xmlsqlinjection_bindings',
            'description': 'xmlsqlinjection bindings',
            'binding_object': 'appfwprofile_xmlsqlinjection_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmlvalidationurl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmlvalidationurl_binding.json'),
        binding_dict={
            'binding_key': 'xmlvalidationurl_bindings',
            'description': 'xmlvalidationurl bindings',
            'binding_object': 'appfwprofile_xmlvalidationurl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmlwsiurl bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmlwsiurl_binding.json'),
        binding_dict={
            'binding_key': 'xmlwsiurl_bindings',
            'description': 'xmlwsiurl bindings',
            'binding_object': 'appfwprofile_xmlwsiurl_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    # xmlxss bindings
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwprofile_xmlxss_binding.json'),
        binding_dict={
            'binding_key': 'xmlxss_bindings',
            'description': 'xmlxss bindings',
            'binding_object': 'appfwprofile_xmlxss_binding',
            'get_all_id': 'name',
            'link_to_main': {
                'main_key': 'name',
                'bind_key': 'name',
            },
        }
    )

    print(json.dumps(attributes_config_list, indent=4))
    print('Bindings\n%s' % json.dumps(bindings, indent=4))

    # Populate the template
    populate_template(
        template_dir,
        main_object_doc_list=main_object_doc_list,
        main_nitro_class='appfwprofile',
        main_object_put_id='name',
        attributes_config_list=attributes_config_list,
        bindings=bindings,
    )



if __name__ == '__main__':
    main()
