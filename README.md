# 2분기 세미나 — Q&A 통합 관리 플랫폼

여러 서비스의 문의를 접수부터 답변·개발 이슈·완료 확인까지 연결하는 Q&A 플랫폼 소개 자료입니다.

## 자료

- [문서 검토 및 내용 정리](notes/content-review.md)
- [발표 구성안](notes/storyboard.md)
- [발표 초안](docs/index.html)

## 검토 기준

제공된 `baron_qa-markdown-docs-2026-09-21.zip`의 Markdown 143개를 추출·목록화하고, 제품 설명·설계·구현 기록·운영 계획을 구분했습니다. 원본과 전체 문서 목차는 로컬 `reference/`에 있습니다. 이 저장소에는 발표용으로 정리한 자료를 관리합니다.

기능 및 검증 결과는 원본 문서에 기록된 내용이며, 이 작업에서 플랫폼 소스 코드나 운영 서비스를 실행해 검증한 결과가 아닙니다. 발표명은 요청하신 ‘2분기 세미나’를 유지하되, 기능 설명의 자료 기준일은 2026-09-21입니다. 2분기 실적 범위는 별도 확정이 필요합니다.

## 화면

`docs/index.html`을 브라우저에서 열면 됩니다. 외부 라이브러리 없이 동작합니다.

- 최대 화면: 7680×2160, 32:9
- 기본안: 발표 / 설명 도식 두 영역, 각각 16:9
- 좌우 방향키: 페이지 이동
- `S`: 분할 / 전체 폭 전환
- `F`: 전체 화면

현재 오른쪽은 문서 기반 설명 도식이며 실제 제품 스크린샷이 아닙니다.
실제 제품 화면·발표자·발표 시간은 다음 편집에서 반영합니다.

검증: Edge의 7680×2160 뷰포트에서 12장 × 2개 보기 모드의 영역 넘침과 키보드 이전·다음 이동 및 페이지 경계를 확인했습니다. 실제 제품 UI와 API는 이번 검증 대상이 아닙니다.

## GitHub Pages

저장소: https://github.com/baron-consultant/disong_QA_seminar

배포 시 사용할 주소: https://baron-consultant.github.io/disong_QA_seminar/

Pages는 `main` 브랜치의 `/docs`만 게시하도록 설정합니다. 이 폴더에는 발표 HTML과 `.nojekyll`만 있습니다. 검토 메모·스크립트·원본 문서는 게시 대상이 아닙니다. 실제 배포 상태는 GitHub Pages 설정과 배포 결과로 확인해야 합니다.

2026-09-22 확인: 저장소는 비공개이며, GitHub API가 현재 요금제에서 이 저장소의 Pages를 지원하지 않는다고 응답했습니다(HTTP 422). 저장소 업로드는 완료했으며 사이트는 아직 게시되지 않았습니다. 비공개 Pages를 지원하는 조직 요금제를 사용하거나, 발표 HTML만 담은 별도 공개 저장소를 사용할 수 있습니다. [GitHub Pages 지원 범위](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
