# Google Drive build: handoff (stopped 2026-10-25)

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

## Done

46 files created (search Drive: `parentId` in the folders above, created after 2026-10-25T09:45Z):
- 44 page Docs, "Website updates needed", "Missing information", "Review for Thalia"
- Sheets "Fleet" (`1xAaw9n6lgAYDYscPHstdBqXWBDkwGtaR42B0PcYBlmk`) and "Decisions" (`1pPSFuuctGyOq4k6toXRZ3Y44a-CsVG9-eDTJ1dDVqaA`)

## Still to do

1. Upload the 9 missing pages (files in `drive/upload/`, title and parent in `manifest.json`):
   policies__check-in, policies__discounts, bases__zea-marina, brokers__commission-and-invoices,
   templates__option-reminder, services__bareboat-charters, services__flotillas,
   services__yacht-management, destinations__kalamos-kastos-atokos.
2. Upload `review_gabi.html` as "Review for Gabi" to the root folder.
3. Verify every file: read it back and check it is complete. Check especially the Fleet and Decisions
   Sheets: their Drive sizes (9 KB and 17 KB) are smaller than the CSVs (45 KB and 55 KB), so the
   uploads may have been cut short. If so, delete nothing; tell the user and re-upload under the same title.
4. Create a "Start here" Doc in the root folder with links to every file.
5. Ask the user for the team's emails and access level before sharing anything.

## How

- Upload: Drive `create_file`, `contentMimeType` `text/html` (Docs) or `text/csv` (Sheets), `textContent` = file content exactly.
- Models: Haiku for uploads and checks; Sonnet only where judgment is needed.
- `drive/upload/` is a snapshot of `kb/` on 2026-10-25. If `kb/` changed since, regenerate with `drive/to_drive.py`
  (needs `pip install markdown`).
- Later syncs need the Google Docs and Google Sheets connectors so files keep the same link.
