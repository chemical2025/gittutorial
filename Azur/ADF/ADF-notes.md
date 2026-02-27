# Azure Data Factory (ADF) — Notes

## Overview
A central place for important ADF concepts, commands, and examples.

## Quick Cheats
- **Heading:** Use `#`, `##`, `###`
- **Bold:** `**Important**`
- **Italic:** `*emphasis*`
- **Highlight (renderers may vary):** `<mark>highlight</mark>`
- **Code:** ````
az datafactory pipeline create --name MyPipeline
````

## Key Concepts
- **Linked Services:** connection information to data stores
- **Datasets:** data structures pointing to data in linked services
- **Pipelines:** orchestration of activities
- **Activities:** units of work (Copy, Data Flow, Lookup, etc.)
- **Triggers:** schedule or event-based pipeline runs
- **Integration Runtime (IR):** compute for data movement and transformations

## Common Tasks
### Create a pipeline (CLI)
```bash
az datafactory pipeline create --resource-group MyRG --factory-name MyFactory --name MyPipeline --pipeline @pipeline.json
```

### Copy activity example (snippet)
```json
{
  "name": "CopyFromBlobToSql",
  "type": "Copy",
  "inputs": [ { "referenceName": "BlobDataset", "type": "DatasetReference" } ],
  "outputs": [ { "referenceName": "SqlDataset", "type": "DatasetReference" } ]
}
```

## Tips
- Use **headings** for sections, **bold** for key points, and `<mark>` for visual highlights in rendered view.
- Add screenshots or diagrams as images for architecture notes.
- Keep CLI snippets runnable and short.
- Use task lists to track follow-ups: `- [ ]` or `- [x]`.

## Useful Links
- Microsoft Docs: https://learn.microsoft.com/azure/data-factory
- ADF Samples repo: https://github.com/Azure/Azure-DataFactory

## TODO
- [ ] Add pipeline debugging checklist
- [ ] Add common error codes & fixes

---
Created: `ADF-notes.md` — feel free to edit and tell me any additions.
