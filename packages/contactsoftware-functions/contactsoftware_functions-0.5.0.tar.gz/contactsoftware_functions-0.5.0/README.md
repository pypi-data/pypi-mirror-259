 <h1><a href="https://github.com/cslab/functions-sdk"><img src="https://www.contact-software.com/design/img/logo-icon.svg" width="50" alt="CONTACT Logo"></a> Functions-Library</h1>

This library is used for creating Functions for CIM Database Cloud.

### Installation

```console
$ pip install contactsoftware-functions
```

### Example usage

```python
from cs.functions import MetaData, WorkloadResponse, Service
from cs.functions.event import DocumentReleaseEvent
from cs.functions.action import AbortAndShowErrorAction


def my_function(metadata: MetaData, event: DocumentReleaseEvent, service: Service):
    number = service.generator.get_number("error_counter")
    message = f"Document {event.data.documents[0].z_nummer} can't be released by {metadata.app_user}! Attempt: {number}"
    return WorkloadResponse(
        event_id=event.event_id,
        actions=[AbortAndShowErrorAction(id="123", message=message)],
    )
```
