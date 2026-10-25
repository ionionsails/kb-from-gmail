# Google Drive build: handoff (stopped twice on 2026-10-25)

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

50 files created (search Drive: `owner = 'me' and createdTime > '2026-10-25T09:45:00Z'`):
- 44 page Docs, "Website updates needed", "Missing information", "Review for Thalia"
- Sheets "Fleet" (`1xAaw9n6lgAYDYscPHstdBqXWBDkwGtaR42B0PcYBlmk`) and "Decisions" (`1pPSFuuctGyOq4k6toXRZ3Y44a-CsVG9-eDTJ1dDVqaA`)
- Session 2 (2026-10-25, 10:09 to 10:12Z) added 4 Docs, not yet read back:
  "Check-in, check-out and documents before arrival" (`1o_q6LdXk2ncsOHeAdPzLGPp22epc-ySuwQ8zohPHDEg`),
  "Bareboat charters" (`1C29_7k3sorAHZr1MDDTF65oIKRmPkryy8NNW2UhD3Bw`),
  "Flotillas (summer, themed, Explorer and Training)" (`1qs2j_ism2JEOAS5PighjwGfayRR6EaWUInC3X6mQOBU`),
  "360 yacht management" (`1_Obv11UBXAB2NMeC9r7kSzfXd23TJcL3amXz57otq3A`)

Verified in session 2:
- Fleet Sheet is A1:T51 and Decisions Sheet is A1:M46. Both match the CSVs exactly (51 x 20 and 46 x 13).
  The smaller Drive sizes are just how Sheets stores data. The Sheets are complete; no re-upload needed.
- "FAQ for direct clients" read back in full: complete.
- Drive size vs text size gave no sign of truncation in the other Docs, but they were not read back yet.

## Still to do

0. Upload agents were stopped mid-run. Before uploading anything, search Drive again (query above)
   and skip any title that already exists, so nothing is duplicated.
1. Upload the 5 missing pages (files in `drive/upload/`, title and parent in `manifest.json`):
   policies__discounts, bases__zea-marina, brokers__commission-and-invoices,
   templates__option-reminder, destinations__kalamos-kastos-atokos.
2. Upload `review_gabi.html` as "Review for Gabi" to the root folder.
3. Verify every Doc: read it back and check it ends with the source text.
   `drive/verify_list.txt` has the 44 older Docs: `fileId | title | expected ending`.
   Add the 4 Docs above and the new uploads. If one is cut short, delete nothing; tell the user
   and re-upload under the same title.
4. Create a "Start here" Doc in the root folder with links to every file.
5. Ask the user for the team's emails and access level before sharing anything.

## How

- Upload: Drive `create_file`, `contentMimeType` `text/html` (Docs) or `text/csv` (Sheets), `textContent` = file content exactly.
- Models: Haiku for uploads and checks; Sonnet only where judgment is needed.
- `drive/upload/` is a snapshot of `kb/` on 2026-10-25. If `kb/` changed since, regenerate with `drive/to_drive.py`
  (needs `pip install markdown`).
- Later syncs need the Google Docs and Google Sheets connectors so files keep the same link.
