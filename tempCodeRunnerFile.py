import docutils.core
  
docutils.core.publish_file(
    source_path='C:\\Users\\QavamS\\Downloads\\Compressed\\rst\\example\\first.rst',
    destination_path='C:\\Users\\QavamS\\Downloads\\Compressed\\rst\\example\\first.html',
    writer_name ="html",
    settings_overrides={'input_encoding': 'UTF-8', 'output_encoding': 'UTF-8'}
    )
