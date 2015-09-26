// Copyright (c) 2011-2014 The CM_UppercaseCoinName developers
// Distributed under the MIT/X11 software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#include "CM_LowercaseCoinNameamountfield.h"

#include "CM_LowercaseCoinNameunits.h"
#include "guiconstants.h"
#include "qvaluecombobox.h"

#include <QApplication>
#include <QDoubleSpinBox>
#include <QHBoxLayout>
#include <QKeyEvent>
#include <qmath.h> // for qPow()

CM_UppercaseCoinNameAmountField::CM_UppercaseCoinNameAmountField(QWidget *parent) :
    QWidget(parent),
    amount(0),
    currentUnit(-1)
{
    nSingleStep = 100000; // satoshis

    amount = new QDoubleSpinBox(this);
    amount->setLocale(QLocale::c());
    amount->installEventFilter(this);
    amount->setMaximumWidth(170);

    QHBoxLayout *layout = new QHBoxLayout(this);
    layout->addWidget(amount);
    unit = new QValueComboBox(this);
    unit->setModel(new CM_UppercaseCoinNameUnits(this));
    layout->addWidget(unit);
    layout->addStretch(1);
    layout->setContentsMargins(0,0,0,0);

    setLayout(layout);

    setFocusPolicy(Qt::TabFocus);
    setFocusProxy(amount);

    // If one if the widgets changes, the combined content changes as well
    connect(amount, SIGNAL(valueChanged(QString)), this, SIGNAL(textChanged()));
    connect(unit, SIGNAL(currentIndexChanged(int)), this, SLOT(unitChanged(int)));

    // Set default based on configuration
    unitChanged(unit->currentIndex());
}

void CM_UppercaseCoinNameAmountField::setText(const QString &text)
{
    if (text.isEmpty())
        amount->clear();
    else
        amount->setValue(text.toDouble());
}

void CM_UppercaseCoinNameAmountField::clear()
{
    amount->clear();
    unit->setCurrentIndex(0);
}

bool CM_UppercaseCoinNameAmountField::validate()
{
    bool valid = true;
    if (amount->value() == 0.0)
        valid = false;
    else if (!CM_UppercaseCoinNameUnits::parse(currentUnit, text(), 0))
        valid = false;
    else if (amount->value() > CM_UppercaseCoinNameUnits::maxAmount(currentUnit))
        valid = false;

    setValid(valid);

    return valid;
}

void CM_UppercaseCoinNameAmountField::setValid(bool valid)
{
    if (valid)
        amount->setStyleSheet("");
    else
        amount->setStyleSheet(STYLE_INVALID);
}

QString CM_UppercaseCoinNameAmountField::text() const
{
    if (amount->text().isEmpty())
        return QString();
    else
        return amount->text();
}

bool CM_UppercaseCoinNameAmountField::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::FocusIn)
    {
        // Clear invalid flag on focus
        setValid(true);
    }
    else if (event->type() == QEvent::KeyPress || event->type() == QEvent::KeyRelease)
    {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        if (keyEvent->key() == Qt::Key_Comma)
        {
            // Translate a comma into a period
            QKeyEvent periodKeyEvent(event->type(), Qt::Key_Period, keyEvent->modifiers(), ".", keyEvent->isAutoRepeat(), keyEvent->count());
            QApplication::sendEvent(object, &periodKeyEvent);
            return true;
        }
    }
    return QWidget::eventFilter(object, event);
}

QWidget *CM_UppercaseCoinNameAmountField::setupTabChain(QWidget *prev)
{
    QWidget::setTabOrder(prev, amount);
    QWidget::setTabOrder(amount, unit);
    return unit;
}

qint64 CM_UppercaseCoinNameAmountField::value(bool *valid_out) const
{
    qint64 val_out = 0;
    bool valid = CM_UppercaseCoinNameUnits::parse(currentUnit, text(), &val_out);
    if (valid_out)
    {
        *valid_out = valid;
    }
    return val_out;
}

void CM_UppercaseCoinNameAmountField::setValue(qint64 value)
{
    setText(CM_UppercaseCoinNameUnits::format(currentUnit, value));
}

void CM_UppercaseCoinNameAmountField::setReadOnly(bool fReadOnly)
{
    amount->setReadOnly(fReadOnly);
    unit->setEnabled(!fReadOnly);
}

void CM_UppercaseCoinNameAmountField::unitChanged(int idx)
{
    // Use description tooltip for current unit for the combobox
    unit->setToolTip(unit->itemData(idx, Qt::ToolTipRole).toString());

    // Determine new unit ID
    int newUnit = unit->itemData(idx, CM_UppercaseCoinNameUnits::UnitRole).toInt();

    // Parse current value and convert to new unit
    bool valid = false;
    qint64 currentValue = value(&valid);

    currentUnit = newUnit;

    // Set max length after retrieving the value, to prevent truncation
    amount->setDecimals(CM_UppercaseCoinNameUnits::decimals(currentUnit));
    amount->setMaximum(qPow(10, CM_UppercaseCoinNameUnits::amountDigits(currentUnit)) - qPow(10, -amount->decimals()));
    amount->setSingleStep((double)nSingleStep / (double)CM_UppercaseCoinNameUnits::factor(currentUnit));

    if (valid)
    {
        // If value was valid, re-place it in the widget with the new unit
        setValue(currentValue);
    }
    else
    {
        // If current value is invalid, just clear field
        setText("");
    }
    setValid(true);
}

void CM_UppercaseCoinNameAmountField::setDisplayUnit(int newUnit)
{
    unit->setValue(newUnit);
}

void CM_UppercaseCoinNameAmountField::setSingleStep(qint64 step)
{
    nSingleStep = step;
    unitChanged(unit->currentIndex());
}
