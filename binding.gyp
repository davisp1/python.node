{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.cc",
        "src/utils.cc",
        "src/py_object_wrapper.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
            "xcode_settings": {
              "OTHER_CFLAGS": [
                "-Wno-error=unused-command-line-argument",
                "<!(python-config --cflags)"
              ],
              "OTHER_LDFLAGS": [
                "<!(python-config --ldflags)"
              ]
            }
        },
        'OS=="win"',{ # win
            'msvs_settings':{
              "VCCLCompilerTool": {
              },
              "VCLibrarianTool": {
              },
              'include_dirs':[
                  "<!(py cflags.py)"
              ],
              'libraries':[
                  "<!(py libs.py)"
              ]
            }
        },
        { # linux
          "cflags": [
            "<!(python-config --cflags)"
          ],
          "libraries": [
            "<!(python-config --libs)"
          ]
        }]
      ]
    }
  ]
}
