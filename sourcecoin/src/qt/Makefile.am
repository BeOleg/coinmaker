include $(top_srcdir)/src/Makefile.include

AM_CPPFLAGS += -I$(top_srcdir)/src \
  -I$(top_builddir)/src/qt \
  -I$(top_builddir)/src/qt/forms \
  $(PROTOBUF_CFLAGS) \
  $(QR_CFLAGS)
bin_PROGRAMS = CM_LowercaseCoinName-qt
noinst_LIBRARIES = libCM_LowercaseCoinNameqt.a
SUBDIRS = . $(BUILD_TEST_QT)
DIST_SUBDIRS = . test

# CM_LowercaseCoinName qt core #
QT_TS = \
  locale/CM_LowercaseCoinName_ach.ts \
  locale/CM_LowercaseCoinName_af_ZA.ts \
  locale/CM_LowercaseCoinName_ar.ts \
  locale/CM_LowercaseCoinName_be_BY.ts \
  locale/CM_LowercaseCoinName_bg.ts \
  locale/CM_LowercaseCoinName_bs.ts \
  locale/CM_LowercaseCoinName_ca_ES.ts \
  locale/CM_LowercaseCoinName_ca.ts \
  locale/CM_LowercaseCoinName_ca@valencia.ts \
  locale/CM_LowercaseCoinName_cmn.ts \
  locale/CM_LowercaseCoinName_cs.ts \
  locale/CM_LowercaseCoinName_cy.ts \
  locale/CM_LowercaseCoinName_da.ts \
  locale/CM_LowercaseCoinName_de.ts \
  locale/CM_LowercaseCoinName_el_GR.ts \
  locale/CM_LowercaseCoinName_en.ts \
  locale/CM_LowercaseCoinName_eo.ts \
  locale/CM_LowercaseCoinName_es_CL.ts \
  locale/CM_LowercaseCoinName_es_DO.ts \
  locale/CM_LowercaseCoinName_es_MX.ts \
  locale/CM_LowercaseCoinName_es.ts \
  locale/CM_LowercaseCoinName_es_UY.ts \
  locale/CM_LowercaseCoinName_et.ts \
  locale/CM_LowercaseCoinName_eu_ES.ts \
  locale/CM_LowercaseCoinName_fa_IR.ts \
  locale/CM_LowercaseCoinName_fa.ts \
  locale/CM_LowercaseCoinName_fi.ts \
  locale/CM_LowercaseCoinName_fr_CA.ts \
  locale/CM_LowercaseCoinName_fr.ts \
  locale/CM_LowercaseCoinName_gl.ts \
  locale/CM_LowercaseCoinName_gu_IN.ts \
  locale/CM_LowercaseCoinName_he.ts \
  locale/CM_LowercaseCoinName_hi_IN.ts \
  locale/CM_LowercaseCoinName_hr.ts \
  locale/CM_LowercaseCoinName_hu.ts \
  locale/CM_LowercaseCoinName_id_ID.ts \
  locale/CM_LowercaseCoinName_it.ts \
  locale/CM_LowercaseCoinName_ja.ts \
  locale/CM_LowercaseCoinName_ka.ts \
  locale/CM_LowercaseCoinName_kk_KZ.ts \
  locale/CM_LowercaseCoinName_ko_KR.ts \
  locale/CM_LowercaseCoinName_ky.ts \
  locale/CM_LowercaseCoinName_la.ts \
  locale/CM_LowercaseCoinName_lt.ts \
  locale/CM_LowercaseCoinName_lv_LV.ts \
  locale/CM_LowercaseCoinName_mn.ts \
  locale/CM_LowercaseCoinName_ms_MY.ts \
  locale/CM_LowercaseCoinName_nb.ts \
  locale/CM_LowercaseCoinName_nl.ts \
  locale/CM_LowercaseCoinName_pam.ts \
  locale/CM_LowercaseCoinName_pl.ts \
  locale/CM_LowercaseCoinName_pt_BR.ts \
  locale/CM_LowercaseCoinName_pt_PT.ts \
  locale/CM_LowercaseCoinName_ro_RO.ts \
  locale/CM_LowercaseCoinName_ru.ts \
  locale/CM_LowercaseCoinName_sah.ts \
  locale/CM_LowercaseCoinName_sk.ts \
  locale/CM_LowercaseCoinName_sl_SI.ts \
  locale/CM_LowercaseCoinName_sq.ts \
  locale/CM_LowercaseCoinName_sr.ts \
  locale/CM_LowercaseCoinName_sv.ts \
  locale/CM_LowercaseCoinName_th_TH.ts \
  locale/CM_LowercaseCoinName_tr.ts \
  locale/CM_LowercaseCoinName_uk.ts \
  locale/CM_LowercaseCoinName_ur_PK.ts \
  locale/CM_LowercaseCoinName_uz@Cyrl.ts \
  locale/CM_LowercaseCoinName_vi.ts \
  locale/CM_LowercaseCoinName_vi_VN.ts \
  locale/CM_LowercaseCoinName_zh_CN.ts \
  locale/CM_LowercaseCoinName_zh_HK.ts \
  locale/CM_LowercaseCoinName_zh_TW.ts

QT_FORMS_UI = \
  forms/aboutdialog.ui \
  forms/addressbookpage.ui \
  forms/askpassphrasedialog.ui \
  forms/coincontroldialog.ui \
  forms/editaddressdialog.ui \
  forms/helpmessagedialog.ui \
  forms/intro.ui \
  forms/openuridialog.ui \
  forms/optionsdialog.ui \
  forms/overviewpage.ui \
  forms/receivecoinsdialog.ui \
  forms/receiverequestdialog.ui \
  forms/rpcconsole.ui \
  forms/sendcoinsdialog.ui \
  forms/sendcoinsentry.ui \
  forms/signverifymessagedialog.ui \
  forms/transactiondescdialog.ui

QT_MOC_CPP = \
  moc_addressbookpage.cpp \
  moc_addresstablemodel.cpp \
  moc_askpassphrasedialog.cpp \
  moc_CM_LowercaseCoinNameaddressvalidator.cpp \
  moc_CM_LowercaseCoinNameamountfield.cpp \
  moc_CM_LowercaseCoinNamegui.cpp \
  moc_CM_LowercaseCoinNameunits.cpp \
  moc_clientmodel.cpp \
  moc_coincontroldialog.cpp \
  moc_coincontroltreewidget.cpp \
  moc_csvmodelwriter.cpp \
  moc_editaddressdialog.cpp \
  moc_guiutil.cpp \
  moc_intro.cpp \
  moc_macdockiconhandler.cpp \
  moc_macnotificationhandler.cpp \
  moc_monitoreddatamapper.cpp \
  moc_notificator.cpp \
  moc_openuridialog.cpp \
  moc_optionsdialog.cpp \
  moc_optionsmodel.cpp \
  moc_overviewpage.cpp \
  moc_paymentserver.cpp \
  moc_qvalidatedlineedit.cpp \
  moc_qvaluecombobox.cpp \
  moc_receivecoinsdialog.cpp \
  moc_receiverequestdialog.cpp \
  moc_recentrequeststablemodel.cpp \
  moc_rpcconsole.cpp \
  moc_sendcoinsdialog.cpp \
  moc_sendcoinsentry.cpp \
  moc_signverifymessagedialog.cpp \
  moc_splashscreen.cpp \
  moc_trafficgraphwidget.cpp \
  moc_transactiondesc.cpp \
  moc_transactiondescdialog.cpp \
  moc_transactionfilterproxy.cpp \
  moc_transactiontablemodel.cpp \
  moc_transactionview.cpp \
  moc_utilitydialog.cpp \
  moc_walletframe.cpp \
  moc_walletmodel.cpp \
  moc_walletview.cpp

CM_AllCapsCoinName_MM = \
  macdockiconhandler.mm \
  macnotificationhandler.mm

QT_MOC = \
  CM_LowercaseCoinName.moc \
  intro.moc \
  overviewpage.moc \
  rpcconsole.moc

QT_QRC_CPP = qrc_CM_LowercaseCoinName.cpp
QT_QRC = CM_LowercaseCoinName.qrc

PROTOBUF_CC = paymentrequest.pb.cc
PROTOBUF_H = paymentrequest.pb.h
PROTOBUF_PROTO = paymentrequest.proto

CM_AllCapsCoinName_QT_H = \
  addressbookpage.h \
  addresstablemodel.h \
  askpassphrasedialog.h \
  CM_LowercaseCoinNameaddressvalidator.h \
  CM_LowercaseCoinNameamountfield.h \
  CM_LowercaseCoinNamegui.h \
  CM_LowercaseCoinNameunits.h \
  clientmodel.h \
  coincontroldialog.h \
  coincontroltreewidget.h \
  csvmodelwriter.h \
  editaddressdialog.h \
  guiconstants.h \
  guiutil.h \
  intro.h \
  macdockiconhandler.h \
  macnotificationhandler.h \
  monitoreddatamapper.h \
  notificator.h \
  openuridialog.h \
  optionsdialog.h \
  optionsmodel.h \
  overviewpage.h \
  paymentrequestplus.h \
  paymentserver.h \
  qvalidatedlineedit.h \
  qvaluecombobox.h \
  receivecoinsdialog.h \
  receiverequestdialog.h \
  recentrequeststablemodel.h \
  rpcconsole.h \
  sendcoinsdialog.h \
  sendcoinsentry.h \
  signverifymessagedialog.h \
  splashscreen.h \
  trafficgraphwidget.h \
  transactiondesc.h \
  transactiondescdialog.h \
  transactionfilterproxy.h \
  transactionrecord.h \
  transactiontablemodel.h \
  transactionview.h \
  utilitydialog.h \
  walletframe.h \
  walletmodel.h \
  walletmodeltransaction.h \
  walletview.h \
  winshutdownmonitor.h

RES_ICONS = \
  res/icons/add.png \
  res/icons/address-book.png \
  res/icons/CM_LowercaseCoinName.ico \
  res/icons/CM_LowercaseCoinName.png \
  res/icons/CM_LowercaseCoinName_testnet.ico \
  res/icons/CM_LowercaseCoinName_testnet.png \
  res/icons/clock1.png \
  res/icons/clock2.png \
  res/icons/clock3.png \
  res/icons/clock4.png \
  res/icons/clock5.png \
  res/icons/configure.png \
  res/icons/connect0_16.png \
  res/icons/connect1_16.png \
  res/icons/connect2_16.png \
  res/icons/connect3_16.png \
  res/icons/connect4_16.png \
  res/icons/debugwindow.png \
  res/icons/edit.png \
  res/icons/editcopy.png \
  res/icons/editpaste.png \
  res/icons/export.png \
  res/icons/filesave.png \
  res/icons/history.png \
  res/icons/key.png \
  res/icons/lock_closed.png \
  res/icons/lock_open.png \
  res/icons/overview.png \
  res/icons/qrcode.png \
  res/icons/quit.png \
  res/icons/receive.png \
  res/icons/remove.png \
  res/icons/send.png \
  res/icons/synced.png \
  res/icons/toolbar.png \
  res/icons/toolbar_testnet.png \
  res/icons/transaction0.png \
  res/icons/transaction2.png \
  res/icons/transaction_conflicted.png \
  res/icons/tx_inout.png \
  res/icons/tx_input.png \
  res/icons/tx_output.png \
  res/icons/tx_mined.png

CM_AllCapsCoinName_QT_CPP = \
  CM_LowercaseCoinName.cpp \
  CM_LowercaseCoinNameaddressvalidator.cpp \
  CM_LowercaseCoinNameamountfield.cpp \
  CM_LowercaseCoinNamegui.cpp \
  CM_LowercaseCoinNameunits.cpp \
  clientmodel.cpp \
  csvmodelwriter.cpp \
  guiutil.cpp \
  intro.cpp \
  monitoreddatamapper.cpp \
  notificator.cpp \
  optionsdialog.cpp \
  optionsmodel.cpp \
  qvalidatedlineedit.cpp \
  qvaluecombobox.cpp \
  rpcconsole.cpp \
  splashscreen.cpp \
  trafficgraphwidget.cpp \
  utilitydialog.cpp \
  winshutdownmonitor.cpp

if ENABLE_WALLET
CM_AllCapsCoinName_QT_CPP += \
  addressbookpage.cpp \
  addresstablemodel.cpp \
  askpassphrasedialog.cpp \
  coincontroldialog.cpp \
  coincontroltreewidget.cpp \
  editaddressdialog.cpp \
  openuridialog.cpp \
  overviewpage.cpp \
  paymentrequestplus.cpp \
  paymentserver.cpp \
  receivecoinsdialog.cpp \
  receiverequestdialog.cpp \
  recentrequeststablemodel.cpp \
  sendcoinsdialog.cpp \
  sendcoinsentry.cpp \
  signverifymessagedialog.cpp \
  transactiondesc.cpp \
  transactiondescdialog.cpp \
  transactionfilterproxy.cpp \
  transactionrecord.cpp \
  transactiontablemodel.cpp \
  transactionview.cpp \
  walletframe.cpp \
  walletmodel.cpp \
  walletmodeltransaction.cpp \
  walletview.cpp
endif

RES_IMAGES = \
  res/images/about.png \
  res/images/splash.png \
  res/images/splash_testnet.png

RES_MOVIES = $(wildcard res/movies/spinner-*.png)

CM_AllCapsCoinName_RC = res/CM_LowercaseCoinName-qt-res.rc

libCM_LowercaseCoinNameqt_a_CPPFLAGS = $(AM_CPPFLAGS) $(QT_INCLUDES) \
  -I$(top_srcdir)/src/qt/forms $(QT_DBUS_INCLUDES)
libCM_LowercaseCoinNameqt_a_SOURCES = $(CM_AllCapsCoinName_QT_CPP) $(CM_AllCapsCoinName_QT_H) $(QT_FORMS_UI) \
  $(QT_QRC) $(QT_TS) $(PROTOBUF_PROTO) $(RES_ICONS) $(RES_IMAGES) $(RES_MOVIES)

nodist_libCM_LowercaseCoinNameqt_a_SOURCES = $(QT_MOC_CPP) $(QT_MOC) $(PROTOBUF_CC) \
  $(PROTOBUF_H) $(QT_QRC_CPP)

BUILT_SOURCES = $(nodist_libCM_LowercaseCoinNameqt_a_SOURCES)

#Generating these with a half-written protobuf header leads to wacky results.
#This makes sure it's done.
$(QT_MOC): $(PROTOBUF_H)
$(QT_MOC_CPP): $(PROTOBUF_H)

# CM_LowercaseCoinName-qt binary #
CM_LowercaseCoinName_qt_CPPFLAGS = $(AM_CPPFLAGS) $(QT_INCLUDES) \
  -I$(top_srcdir)/src/qt/forms
CM_LowercaseCoinName_qt_SOURCES = CM_LowercaseCoinName.cpp
if TARGET_DARWIN
  CM_LowercaseCoinName_qt_SOURCES += $(CM_AllCapsCoinName_MM)
endif
if TARGET_WINDOWS
  CM_LowercaseCoinName_qt_SOURCES += $(CM_AllCapsCoinName_RC)
endif
CM_LowercaseCoinName_qt_LDADD = libCM_LowercaseCoinNameqt.a $(LIBCM_AllCapsCoinName_SERVER)
if ENABLE_WALLET
CM_LowercaseCoinName_qt_LDADD += $(LIBCM_AllCapsCoinName_WALLET)
endif
CM_LowercaseCoinName_qt_LDADD += $(LIBCM_AllCapsCoinName_CLI) $(LIBCM_AllCapsCoinName_COMMON) $(LIBLEVELDB) $(LIBMEMENV) \
  $(BOOST_LIBS) $(QT_LIBS) $(QT_DBUS_LIBS) $(QR_LIBS) $(PROTOBUF_LIBS) $(BDB_LIBS)
CM_LowercaseCoinName_qt_LDFLAGS = $(QT_LDFLAGS)

# forms/foo.h -> forms/ui_foo.h
QT_FORMS_H=$(join $(dir $(QT_FORMS_UI)),$(addprefix ui_, $(notdir $(QT_FORMS_UI:.ui=.h))))

#locale/foo.ts -> locale/foo.qm
QT_QM=$(QT_TS:.ts=.qm)

.PHONY: FORCE
.SECONDARY: $(QT_QM)

CM_LowercaseCoinNamestrings.cpp: FORCE
	$(MAKE) -C $(top_srcdir)/src qt/CM_LowercaseCoinNamestrings.cpp

translate: CM_LowercaseCoinNamestrings.cpp $(QT_FORMS_UI) $(QT_FORMS_UI) $(CM_AllCapsCoinName_QT_CPP) $(CM_AllCapsCoinName_QT_H) $(CM_AllCapsCoinName_MM)
	@test -n $(LUPDATE) || echo "lupdate is required for updating translations"
	@QT_SELECT=$(QT_SELECT) $(LUPDATE) $^ -locations relative -no-obsolete -ts locale/CM_LowercaseCoinName_en.ts

$(QT_QRC_CPP): $(QT_QRC) $(QT_QM) $(QT_FORMS_H) $(RES_ICONS) $(RES_IMAGES) $(RES_MOVIES) $(PROTOBUF_H)
	@cd $(abs_srcdir); test -f $(RCC) && QT_SELECT=$(QT_SELECT) $(RCC) -name CM_LowercaseCoinName -o $(abs_builddir)/$@ $< || \
	  echo error: could not build $@
	$(SED) -e '/^\*\*.*Created:/d' $@ > $@.n && mv $@{.n,}
	$(SED) -e '/^\*\*.*by:/d' $@  > $@.n && mv $@{.n,}

CLEANFILES = $(BUILT_SOURCES) $(QT_QM) $(QT_FORMS_H) *.gcda *.gcno
