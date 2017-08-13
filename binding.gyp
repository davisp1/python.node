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
            'include_dirs':[
                "C:\\python27\\include"
            ],
            'link_settings':{
                'libraries':[
                    "C:\\python27\\libs\\python27.lib"
                ]
            },
            "msvs_settings": {
                "VCCLCompilerTool": {
                    "RuntimeLibrary": 0,
                    "Optimization": 3,
                    "FavorSizeOrSpeed": 1,
                    "InlineFunctionExpansion": 2,
                    "WholeProgramOptimization": "true",
                    "OmitFramePointers": "true",
                    "EnableFunctionLevelLinking": "true",
                    "EnableIntrinsicFunctions": "true",
                    "RuntimeTypeInfo": "false",
                    "ExceptionHandling": "0",
                    "AdditionalOptions": [
                        "/MP /EHsc"
                    ]
                },
                "VCLibrarianTool": {
                    "AdditionalOptions": [
                        "/LTCG"
                    ]
                },
                "VCLinkerTool": {
                    "LinkTimeCodeGeneration": 1,
                    "OptimizeReferences": 2,
                    "EnableCOMDATFolding": 2,
                    "LinkIncremental": 1,
                }
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
