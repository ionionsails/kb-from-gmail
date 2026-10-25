# Google Drive build: handoff

The wiki in `kb/` is published to Google Drive (account info@ionionsails.com) as Docs and Sheets
so Thalia (CEO) and Gabi (owner) can review it. The build was stopped part-way to start a new session.
Nothing is shared with anyone yet.

## Drive folders

| Folder | ID |
| --- | --- |
| IonionSails Sales KB (root) | `1ZCaswAu3LZu-kkWSQRe14EJQSGTr4oOS` |
| Policies | `1Yze1BK9LcdmWBmCmXKvqtJzGEivh-pIp` |
| Bases | `1_9BcFqP63C9mjJLk1RM9e-k3hz2uZBCc` |
| Brokers | `1mP7J0Ar85HyeUx-MaCJAjV_WtInPCwut` |
| FAQ | `1NLgNVBfqvLtl1LCYdrH3QQ18PrfKDSu_` |
| Templates | `192_dhsl6o666_mO8SjnQ_uHVt08hTBWf` |
| Services | `1MFA0fIbn6qygX3hB0mqpNjVbNqOF5wxT` |
| Destinations | `1FrIpNStFxYrj_Td5dphmWdSPMblAyRjz` |
| Company | `1qKhE9US6qc1PINpe70XDJHd0hyNG5TkX` |

## Done (build finished 2026-10-25)

58 files in Drive, all read back and complete. Nothing is shared with anyone yet.
- "Start here" Doc in the root folder (`1Bvnu0hKv-XibYFkuGLoUZofluoyAD0FnGRjNzDDOF0g`), with links to all 57 other files
- 55 Docs: 51 wiki pages, "Website updates needed", "Missing information", "Review for Thalia", "Review for Gabi"
- Sheets "Fleet" (`1xAaw9n6lgAYDYscPHstdBqXWBDkwGtaR42B0PcYBlmk`, A1:T51) and
  "Decisions" (`1pPSFuuctGyOq4k6toXRZ3Y44a-CsVG9-eDTJ1dDVqaA`, A1:M46). Both match the CSVs exactly.
- `verify_list.txt` has every Doc (except Zea Marina, checked by hand): `fileId | title | expected ending`.
  Every Doc ends with its source text. `upload/start_here.html` is the source of "Start here".

## Still to do

1. Ask the user for the team's emails and access level before sharing anything.
2. Later syncs: update files in place so links stay the same (Drive `update_file`, or the
   Google Docs and Google Sheets connectors). Do not create new copies.

## How

- Upload: Drive `create_file`, `contentMimeType` `text/html` (Docs) or `text/csv` (Sheets), `textContent` = file content exactly.
- Models: Haiku for uploads and checks; Sonnet only where judgment is needed.
- `drive/upload/` is a snapshot of `kb/` on 2026-10-25. If `kb/` changed since, regenerate with `drive/to_drive.py`
  (needs `pip install markdown`).
- Later syncs need the Google Docs and Google Sheets connectors so files keep the same link.
