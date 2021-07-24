 #!/bin/bash
 name="myfirstdockerimage"
 docker build . -t ${name}
 docker tag ${name} us.gcr.io/<project>/${name}
 docker push us.gcr.io/<project>/${name}


